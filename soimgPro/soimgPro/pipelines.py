# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class SoimgproPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        print(request.url)
        return request.url.split('/')[-1]

    def get_media_requests(self, item, info):
        #  adapter = ItemAdapter(item)
        #  print(item)
        for url in item['urls']:
            print(url)
            yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        print(item)
        return item
