# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhotographyTipsScraperItem(scrapy.Item):
    title = scrapy.Field(default=None)
    content = scrapy.Field(default=None)
    url = scrapy.Field(default=None)
    images_url = scrapy.Field(default=None)
    article_tags = scrapy.Field(default=None)