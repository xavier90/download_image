# coding:utf-8
# 需要安装pillow模块
import scrapy
from items import DecItem

# from scrapy.crawler import CrawlerProcess


class DecSpider(scrapy.Spider):
    name = 'ScrapyDec'
    allowed_domains = []
    start_urls = ["http://www.decormatters.com/index.php"]

    def parse(self, response):
        item = DecItem()
        item['image_urls'] = response.xpath('//img//@src').extract()  # 提取图片链接
        print 'image_urls',item['image_urls']
        yield item
        # new_url = response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()  # 翻页
        # # print 'new_url',new_url
        # if new_url:
        #     yield scrapy.Request(new_url, callback=self.parse)
