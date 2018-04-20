# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanMovieItem(scrapy.Item):
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()


class WorldCupItem(scrapy.Item):
    time = scrapy.Field()
    fieldorder = scrapy.Field()
    match = scrapy.Field()
    city = scrapy.Field()
