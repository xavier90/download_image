# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DecItem(scrapy.Item):
    # define the fields for your item here like:

    images = scrapy.Field()

    storeName = scrapy.Field()
    categoryName = scrapy.Field()
    categoryId = scrapy.Field()
    subCategoryId = scrapy.Field()
    storeId = scrapy.Field()
    productUrl = scrapy.Field()
    salePrice = scrapy.Field()
    title = scrapy.Field()

    description = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    depth = scrapy.Field()

    imageUrls = scrapy.Field()
    awsImageUrls = scrapy.Field()
    thumbImageUrl = scrapy.Field()

    keywords = scrapy.Field()

    color = scrapy.Field()
    address = scrapy.Field()
    sku = scrapy.Field()
