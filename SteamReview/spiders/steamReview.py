import scrapy
from scrapy.loader import ItemLoader
from SteamReview.items import Review, ReviewItemLoader
import json
from scrapy.loader.processors import TakeFirst

page_number = 1
filename = 'reviews.txt'
# app_id = '1061090'
api_url = 'https://steamcommunity.com/app/{0}/homecontent/?userreviewsoffset=10&'\
            'p={1}&workshopitemspage={1}&readytouseitemspage={1}&mtxitemspage={1}&'\
            'itemspage={1}&screenshotspage={1}&videospage={1}&artpage={1}&'\
            'allguidepage={1}&webguidepage={1}&integratedguidepage={1}&'\
            'discussionspage={1}&numperpage=10&browsefilter=toprated&'\
            'browsefilter=toprated&l=english&appHubSubSection=10&'\
            'filterLanguage=default&searchText=&forceanon=1'\


class SteamReviews(scrapy.Spider):
    name = 'steamReview'

    def __init__(self, appid='1061090', **kwargs):
        self.start_urls = [api_url.format(appid, page_number)]
        super().__init__(**kwargs)

    def parse(self, response):
        reviews = response.css('.apphub_CardContentMain')

        for review in reviews:
            reviewLoader = ItemLoader(item=Review(), selector=review)

            reviewLoader.add_css('recommendedInd', '.title::text')

            # # Peer review ratings
            reviewLoader.add_css('helpfulCount', '.found_helpful ::text', re='([\d,]+).*helpful')
            reviewLoader.add_css('funnyCount', '.found_helpful ::text', re='([\d,]+).*funny')

            reviewLoader.add_css('hoursPlayed', '.hours::text', re='(.+) hrs')
            reviewLoader.add_css('postedDate', '.date_posted::text')
            reviewLoader.add_css('responseCount', '.apphub_CardCommentCount ::text')
            reviewLoader.add_css('content', '.apphub_CardTextContent::text')

            yield reviewLoader.load_item()

        # if reviews['has_next']:
        #     page_number += 1
        #     yield scrapy.Request(url=self.api_url.format(app_id, page_number), callback=self.parse)
