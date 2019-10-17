import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, Join, MapCompose, TakeFirst


# Steam reviews come with special character additions (such as tabs and new lines, we want to remove these)
class CleanText:
    def __init__(self, chars='\r\t\n'):
        self.chars = chars

    def __call__(self, value):
        try:
            return value.strip(self.chars)
        except:
            return value


# Convert values to integers
def convertToInt(x):
    x = x.replace(',', '')
    try:
        return int(x)
    except:
        return x

# Convert values to integers
def convertToFloat(x):
    x = x.replace(',', '')
    try:
        return float(x)
    except:
        return x

class Review(scrapy.Item):
    # The app id for the specified game
    appId = scrapy.Field(
          output_processor=Compose(
             MapCompose(
                 CleanText(),
                 convertToInt),
             max
          )
    )
    appId.setdefault('0')
    # An indicator for whether or not the review was identified as useful
    recommendedInd = scrapy.Field(
         input_processor=MapCompose(CleanText()),
         output_processor=Compose(Join('\n'), CleanText())
    )
    # The number of people who found the review helpful
    helpfulCount = scrapy.Field(
          output_processor=Compose(
              MapCompose(
                  CleanText(),
                  convertToInt),
              max
          )
    )
    helpfulCount.setdefault(0)
    # The number of people who found the review funny
    funnyCount = scrapy.Field(
          output_processor=Compose(
             MapCompose(
                 CleanText(),
                 convertToInt),
             max
          )
    )
    funnyCount.setdefault(0)
    # The number of hours the user played
    hoursPlayed = scrapy.Field(
          output_processor=Compose(
             MapCompose(
                 CleanText(),
                 convertToFloat),
             max
          )
    )
    hoursPlayed.setdefault(0)
    # The date that the review was posted
    postedDate = scrapy.Field()
    # The number of responses on the review
    responseCount = scrapy.Field(
          output_processor=Compose(
             MapCompose(
                 CleanText(),
                 convertToInt),
             max
          )
    )
    responseCount.setdefault(0)
    # The string content of the review
    content = scrapy.Field(
         input_processor=MapCompose(CleanText()),
         output_processor=Compose(Join('\n'), CleanText())
    )

class ReviewItemLoader(ItemLoader):
    default_output_processor = TakeFirst()