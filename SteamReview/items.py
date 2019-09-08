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


class Review(scrapy.Item):
    # An indicator for whether or not the review was identified as useful
    recommendedInd = scrapy.Field()
    # The number of people who found the review helpful
    helpfulCount = scrapy.Field(
         output_processor=Compose(
             MapCompose(
                 CleanText(),
                 lambda x: x.replace(',', ''),
                 convertToInt),
             max
         )
    )
    # The number of people who found the review funny
    funnyCount = scrapy.Field()
    # The number of hours the user played
    hoursPlayed = scrapy.Field()
    # The date that the review was posted
    postedDate = scrapy.Field()
    # The number of responses on the review
    responseCount = scrapy.Field()
    # The string content of the review
    content = scrapy.Field(
         input_processor=MapCompose(CleanText()),
         output_processor=Compose(Join('\n'), CleanText())
    )

class ReviewItemLoader(ItemLoader):
    default_output_processor = TakeFirst()