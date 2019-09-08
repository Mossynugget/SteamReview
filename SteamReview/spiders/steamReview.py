import scrapy
from scrapy.loader import ItemLoader
from SteamReview.items import Review, ReviewItemLoader
from scrapy.loader.processors import TakeFirst

filename = 'reviews.txt'
api_url = 'https://steamcommunity.com/app/{0}/homecontent/?userreviewsoffset=30&p={1}&workshopitemspage={1}'\
          '&readytouseitemspage={1}&mtxitemspage={1}&itemspage={1}&screenshotspage={1}&videospage={1}&artpage={1}'\
          '&allguidepage={1}&webguidepage={1}&integratedguidepage={1}&discussionspage={1}&numperpage=10'\
          '&browsefilter=toprated&browsefilter=toprated&appid={0}&appHubSubSection=10&appHubSubSection=10&l=english'\
          '&filterLanguage=default&searchText=&forceanon=1'


class SteamReviews(scrapy.Spider):
    name = 'steamReview'
    app_id = '379430'
    page_number = 1
    start_urls = [api_url.format(app_id, page_number)]

    def parse(self, response):
        # data = json.loads(response.text)
        reviews = response.css('.apphub_CardContentMain')

        for review in reviews:
            reviewLoader = ItemLoader(item=Review(), selector=review)

            reviewLoader.add_css('recommendedInd', '.title::text')
            #
            # # Peer review ratings
            feedback = reviewLoader.get_css('.found_helpful ::text')
            reviewLoader.add_css('helpfulCount', feedback, re='([\d,]+) of')
            reviewLoader.add_css('funnyCount', feedback, re='([\d,]+).*funny')

            reviewLoader.add_css('hoursPlayed', '.hours::text', re='(.+) hrs')
            reviewLoader.add_css('postedDate', '.date_posted::text')
            reviewLoader.add_css('responseCount', '.apphub_CardCommentCount ::text')
            reviewLoader.add_css('content', '.apphub_CardTextContent::text')
            yield reviewLoader.load_item()

        # if reviews['has_next']:
        #     page_number = data['p'] + 1
        #     app_id = data['appid']
        #     yield scrapy.Request(url=self.api_url.format(app_id, page_number), callback=self.parse)
