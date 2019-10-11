BOT_NAME = 'SteamReview'

SPIDER_MODULES = ['SteamReview.spiders']
NEWSPIDER_MODULE = 'SteamReview.spiders'

FEED_FORMAT = 'json'
FEED_URI = 'tmp/SteamReviews.json'

ROBOTSTXT_OBEY = True

AUTOTHROTTLE_ENABLED = True

# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60

HTTPCACHE_ENABLED = True

ITEM_PIPELINES = {
   'SteamReview.pipelines.postGrePipeLine': 300,
}
