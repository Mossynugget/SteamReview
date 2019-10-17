import psycopg2
from collections import OrderedDict
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from wordcloud import WordCloud
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")


class postGrePipeLine(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(database='SteamReviewScraper',
                                           user='postgres', password='admin', port=5432)

        self.cur = self.connection.cursor()

        self.clearDatabase()

    def close_spider(self, spider):
        wc = WordCloudHelper()

        self.cur.execute(
            "SELECT \"Keyword\", SUM(\"Weighting\")"
            " FROM public.\"NormalizedSentiments\""
            " WHERE \"Weighting\" != double precision 'NaN'"
            " GROUP BY \"Keyword\""
            " ORDER BY SUM(\"Weighting\") DESC "
            " LIMIT 100")
        data = defaultdict(list)
        for record in self.cur:
            data[record[0]] = float(record[1])
            if data[record[0]] > 10:
                data[record[0]] = 10
        if len(data) > 0:
            wc.generateWordCloud(data, 'tmp/WordCloud')

        data.clear()
        self.cur.execute(
            "SELECT \"Keyword\", SUM(\"Weighting\")"
            " FROM public.\"NormalizedSentiments\""
            " WHERE \"Weighting\" != double precision 'NaN'"
            " AND \"Positive\" = 1"
            " GROUP BY \"Keyword\""
            " ORDER BY SUM(\"Weighting\") DESC "
            " LIMIT 100")
        data = defaultdict(list)
        for record in self.cur:
            data[record[0]] = float(record[1])
            if data[record[0]] > 10:
                data[record[0]] = 10

        if len(data) > 0:
            wc.generateWordCloud(data, 'tmp/PositiveWordCloud')

        data.clear()
        self.cur.execute(
            "SELECT \"Keyword\", SUM(\"Weighting\")"
            " FROM public.\"NormalizedSentiments\""
            " WHERE \"Weighting\" != double precision 'NaN'"
            " AND \"Positive\" = 0"
            " GROUP BY \"Keyword\""
            " ORDER BY SUM(\"Weighting\") DESC "
            " LIMIT 100")
        for record in self.cur:
            data[record[0]] = float(record[1])
            if data[record[0]] > 10:
                data[record[0]] = 10

        if len(data) > 0:
            wc.generateWordCloud(data, 'tmp/NegativeWordCloud')

        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        if 'helpfulCount' not in item:
            item['helpfulCount'] = 0

        if 'funnyCount' not in item:
            item['funnyCount'] = 0

        if 'responseCount' not in item:
            item['responseCount'] = 0

        self.cur.execute(
            "INSERT INTO public.\"RawSteamReviews\" (\"RecommendedInd\", \"HelpfulCount\", \"FunnyCount\", "
            "\"HoursPlayed\", \"PostedDate\", \"ResponseCount\", \"Content\", \"AppId\") "
            "VALUES (%(recommendedInd)s, %(helpfulCount)s, %(funnyCount)s, %(hoursPlayed)s, %(postedDate)s, "
            "%(responseCount)s, %(content)s, %(appId)s);", item)

        # id_of_new_row = self.cur.fetchone()[0]
        # print(str(id_of_new_row))
        # results = nlp(item['content'])
        #
        # print([chunk.text for chunk in results.noun_chunks])

        tr4w = TextRank4Keyword()
        tr4w.analyze(item['content'], candidate_pos=['NOUN', 'PROPN'], window_size=4, lower=False)

        print(item['recommendedInd'])

        if "Not" not in item['recommendedInd']:
            positive = 1
        else:
            positive = 0

        keywords = tr4w.get_keywords(10)
        print(keywords);
        for i, (key, value) in enumerate(keywords.items()):
            # Ensure that the item doesn't exist in the blacklist.
            if key not in blacklist:
                self.cur.execute("INSERT INTO public.\"NormalizedSentiments\" (\"Keyword\", "
                                 "\"Weighting\", \"Positive\") VALUES (%s, %s, %s); ", (key, str(value), positive))
                if i > 10:
                    break

        self.connection.commit()
        return item

    def clearDatabase(self):
        self.cur.execute("DELETE FROM public.\"NormalizedSentiments\"")
        self.cur.execute("DELETE FROM public.\"RawSteamReviews\"")
        self.connection.commit()


class WordCloudHelper:
    background_color = "#101010"
    height = 720
    width = 1080

    def generateWordCloud(self, data, filename):
        word_cloud = WordCloud(
            background_color=self.background_color,
            width=self.width,
            height=self.height
        )

        word_cloud.generate_from_frequencies(data)
        word_cloud.to_file(filename+'.png')


class TextRank4Keyword():
    """Extract keywords from text"""

    def __init__(self):
        self.d = 0.85  # damping coefficient, usually is .85
        self.min_diff = 1e-5  # convergence threshold
        self.steps = 10  # iteration steps
        self.node_weight = None  # save keywords and its weight

    def set_stopwords(self, stopwords):
        """Set stop words"""
        for word in STOP_WORDS.union(set(stopwords)):
            lexeme = nlp.vocab[word]
            lexeme.is_stop = True

    def sentence_segment(self, doc, candidate_pos, lower):
        """Store those words only in cadidate_pos"""
        sentences = []
        for sent in doc.sents:
            selected_words = []
            for token in sent:
                # Store words only with candidate POS tag
                if token.pos_ in candidate_pos and token.is_stop is False:
                    if lower is True:
                        selected_words.append(token.text.lower())
                    else:
                        selected_words.append(token.text)
            sentences.append(selected_words)
        return sentences

    def get_vocab(self, sentences):
        """Get all tokens"""
        vocab = OrderedDict()
        i = 0
        for sentence in sentences:
            for word in sentence:
                if word not in vocab:
                    vocab[word] = i
                    i += 1
        return vocab

    def get_token_pairs(self, window_size, sentences):
        """Build token_pairs from windows in sentences"""
        token_pairs = list()
        for sentence in sentences:
            for i, word in enumerate(sentence):
                for j in range(i + 1, i + window_size):
                    if j >= len(sentence):
                        break
                    pair = (word, sentence[j])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        return token_pairs

    def symmetrize(self, a):
        return a + a.T - np.diag(a.diagonal())

    def get_matrix(self, vocab, token_pairs):
        """Get normalized matrix"""
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            i, j = vocab[word1], vocab[word2]
            g[i][j] = 1

        # Get Symmetric matrix
        g = self.symmetrize(g)

        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        g_norm = np.divide(g, norm, where=norm != 0)  # this is ignore the 0 element in norm

        return g_norm

    def get_keywords(self, number=10):
        """Print top number keywords"""
        node_weight = OrderedDict(sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        for i, (key, value) in enumerate(node_weight.items()):
            print(key + ' - ' + str(value))
            if i > number:
                break
        return node_weight

    def analyze(self, text,
                candidate_pos=['NOUN', 'PROPN'],
                window_size=4, lower=False, stopwords=list()):
        """Main function to analyze text"""

        # Set stop words
        self.set_stopwords(stopwords)

        # Pare text by spaCy
        doc = nlp(text)

        # Filter sentences
        sentences = self.sentence_segment(doc, candidate_pos, lower)  # list of list of words

        # Build vocabulary
        vocab = self.get_vocab(sentences)

        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, sentences)

        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)

        # Initionlization for weight(pagerank value)
        pr = np.array([1] * len(vocab))

        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1 - self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr)) < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]

        self.node_weight = node_weight

blacklist = ["game", "Game", "Games", "games"]