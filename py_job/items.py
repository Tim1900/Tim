# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PyJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    compony_name = scrapy.Field()
    salary_range_low = scrapy.Field()
    salary_range_high = scrapy.Field()
    location = scrapy.Field()
    experience = scrapy.Field()
    degree = scrapy.Field()
    description = scrapy.Field()
    welfare = scrapy.Field()
    date_published = scrapy.Field()
