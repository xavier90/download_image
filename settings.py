#
#-*- coding: utf-8 -*-
# Scrapy settings for jiandan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyDec'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ITEM_PIPELINES = {
    'pipelines.DecPipeline': 1,

}
# ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
# ITEM_PIPELINES = {'jiandan.pipelines.ImagesPipeline': 1}
# AWS_ACCESS_KEY_ID = "xxxxxx"
# AWS_SECRET_ACCESS_KEY = "xxxxxx"
#IMAGES_STORE = "s3://decormatters-dev/product-images/"

IMAGES_STORE = "/home/ec2-user/script_test/"

# IMAGES_STORE = '/Users/yaojianwang/Desktop/scrapyTest/img'
DOWNLOAD_DELAY = 0.25

