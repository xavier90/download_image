import json
import scrapy
import hashlib
from items import DecItem
import os
class DecSpider(scrapy.Spider):
    name = 'download_image'
    allowed_domains = []
    start_urls = [
        'https://www.google.com/'
    ]



    def parse(self, response):

        f = open('result_yliving.json')
        data = json.load(f)

        # cmd_bgRemove = "./bgRemover"
        # cmd_removeInputfile = "rm /home/ec2-user/data_big/full/*.jpg"
        # cmd_removeMaskfile = "rm /home/ec2-user/data_big/masks/*.jpg"
        # cmd_moveOutputfileToS3 = "aws s3 mv /home/ec2-user/data_big/output s3://decormatters-dev/product-images/ --recursive --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers full=emailaddress=accounts@decormatters.com"
        #
        # os.system(cmd_bgRemove)

        for line in data:
            # urls = line['imageUrls']

            # awsImageUrls = []
            # for url in urls:
            #     # use hash to generate image file name
            #     hash_url_to_name = hashlib.sha1(url).hexdigest()
            #     awsImageUrls.append("https://s3-us-west-1.amazonaws.com/decormatters-dev/product-images/" + hash_url_to_name + "_final.png")
            #
            #os.system(cmd_bgRemove)
            #os.system(cmd_moveOutputfileToS3)
           # os.system(cmd_removeMaskfile)
            #os.system(cmd_removeInputfile)
            item = DecItem()
            item['storeName'] = line['storeName']
            item['categoryName'] = line['categoryName']
            item['categoryId'] = line['categoryId']
            #if line['subCategoryId']:
             #   item['subCategoryId'] = line['subCategoryId']
            item['storeId'] = line['storeId']
            item['productUrl'] = line['productUrl']
          #  item['salePrice'] = line['salePrice']
            item['title'] = line['title']

            item['description'] = line['description']
            if 'width' in line and 'height' in line:
                item['width'] = line['width']
                item['height'] = line['height']
            if 'depth' in line:
                item['depth'] = line['depth']

            item['imageUrls'] = line['imageUrls']
            item['awsImageUrls'] = line['awsImageUrls']
            item['thumbImageUrl'] = line['thumbImageUrl']

            item['keywords'] = line['keywords']

            item['color'] = line['color']
            item['address'] = line['address']
            #item['sku'] = line['sku']


            yield item
