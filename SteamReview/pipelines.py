import psycopg2


class postGrePipeLine(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(database='SteamReviewScraper',
                                           user='postgres', password='admin', port=5432)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        print("Hello")
        print(item)
        print("Hello")

        if 'helpfulCount' not in item:
            item['helpfulCount'] = 0

        if 'funnyCount' not in item:
            item['funnyCount'] = 0

        if 'responseCount' not in item:
            item['responseCount'] = 0

        print("Hello")
        print(item)
        print("Hello")

        self.cur.execute("INSERT INTO public.\"RawSteamReviews\" (\"RecommendedInd\", \"HelpfulCount\", \"FunnyCount\", " \
                "\"HoursPlayed\", \"PostedDate\", \"ResponseCount\", \"Content\", \"AppId\") " \
                "VALUES (%(recommendedInd)s, %(helpfulCount)s, %(funnyCount)s, %(hoursPlayed)s, %(postedDate)s, " \
                "%(responseCount)s, %(content)s, %(appId)s); ", item)

        # self.cur.execute("INSERT INTO public.\"RawSteamReviews\" (\"RecommendedInd\"" \
        #         "\"HoursPlayed\", \"PostedDate\", \"Content\", \"AppId\") " \
        #         "VALUES (%(recommendedInd)s, %(hoursPlayed)s, %(postedDate)s, " \
        #         "%(content)s, %(appId)s); ", item)
        self.cur.execute("INSERT INTO public.\"RawSteamReviews\" (\"RecommendedInd\", "
                         "\"HoursPlayed\", \"PostedDate\", \"Content\", \"AppId\") "
                         "VALUES (%(recommendedInd)s, %(hoursPlayed)s, %(postedDate)s, "
                         "%(content)s, %(appId)s); ", item)
        self.connection.commit()
        return item
