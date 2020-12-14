# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChartParserItem(scrapy.Item):
    author = scrapy.Field()
    song = scrapy.Field()
    position = scrapy.Field()

