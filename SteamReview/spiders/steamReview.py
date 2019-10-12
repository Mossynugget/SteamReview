import scrapy
import psycopg2
from scrapy.loader import ItemLoader
from SteamReview.items import Review, ReviewItemLoader
import json
from scrapy.loader.processors import TakeFirst

filename = 'reviews.txt'


# app_id = '1061090'

def clearDatabase():
    print("Do something")

def analyseData():
    print("Do something")

class SteamReviews(scrapy.Spider):
    name = 'steamReview'

    api_url = 'https://steamcommunity.com/app/{0}/homecontent/' \
              '?userreviewsoffset={2}&p={1}&workshopitemspage={1}&readytouseitemspage={1}' \
              '&mtxitemspage={1}&itemspage={1}&screenshotspage={1}&videospage={1}' \
              '&artpage={1}&allguidepage={1}&webguidepage={1}&integratedguidepage={1}' \
              '&discussionspage={1}&numperpage=10&browsefilter=toprated&appid={0}' \
              '&appHubSubSection=10&l=english&filterLanguage=default&forceanon=1' \

    appid = ''
    page_number = 1
    page_offset = 10

    def __init__(self, appid='1061090', page_number=1, **kwargs):
        self.appid = appid
        self.page_number = page_number
        self.start_urls = [self.api_url.format(self.appid, self.page_number, self.page_offset)]
        super().__init__(**kwargs)

    def parse(self, response):
        reviews = response.css('.apphub_CardContentMain')
        count = 0

        for review in reviews:
            reviewLoader = ItemLoader(item=Review(), selector=review)

            reviewLoader.add_value('appId', self.appid)
            reviewLoader.add_css('recommendedInd', '.title::text')

            # # Peer review ratings
            reviewLoader.add_css('helpfulCount', '.found_helpful ::text', re='([\d,]+).*helpful')
            reviewLoader.add_css('funnyCount', '.found_helpful ::text', re='([\d,]+).*funny')

            reviewLoader.add_css('hoursPlayed', '.hours::text', re='(.+) hrs')
            reviewLoader.add_css('postedDate', '.date_posted::text', re='Posted: (.+)')
            reviewLoader.add_css('responseCount', '.apphub_CardCommentCount ::text')
            reviewLoader.add_css('content', '.apphub_CardTextContent::text')
            count += 1

            yield reviewLoader.load_item()

        if count != 0:
            self.page_number += 1
            self.page_offset = self.page_number*10-10
            yield scrapy.Request(url=self.api_url.format(self.appid, self.page_number, self.page_offset), callback=self.parse,
                                 meta={'appid': self.appid, 'page_number': self.page_number})
        # else:
        #     analyseData()
