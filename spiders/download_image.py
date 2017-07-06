import json
import scrapy
import hashlib
from items import DecItem

class DecSpider(scrapy.Spider):
    name = 'download_image'
    allowed_domains = []
    start_urls = [
        'https://www.google.com/'
    ]



    def parse(self, response):

        f = open('result_landofnod_0629.json')
        data = json.load(f)

        for line in data:
            urls = line['imageUrls']

            productImages = []
            for url in urls:
                # use hash to generate image file name
                hash_url_to_name = hashlib.sha1(url).hexdigest()
                productImages.append(hash_url_to_name)

            item = DecItem()
            item['storeName'] = line['storeName']
            item['categoryName'] = line['categoryName']
            item['categoryId'] = line['categoryId']
            item['subCategoryId'] = line['subCategoryId']
            item['storeId'] = line['storeId']
            item['productUrl'] = line['productUrl']
            item['salePrice'] = line['salePrice']
            item['title'] = line['title']

            item['description'] = line['description']
            if 'width' in line and 'height' in line:
                item['width'] = line['width']
                item['height'] = line['height']
            if 'depth' in line:
                item['depth'] = line['depth']

            item['imageUrls'] = line['imageUrls']
            item['productImages'] = productImages
            item['thumbImageUrl'] = line['thumbImageUrl']

            item['keywords'] = line['keywords']

            item['color'] = line['color']
            item['address'] = line['address']
            item['sku'] = line['sku']


            yield item
