# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class GithubTrendItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    repo_name = Field()
    repo_description = Field()
    num_stars = Field()
