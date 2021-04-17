import scrapy
from soimgPro.items import ImgItem


class SoimgSpider(scrapy.Spider):
    name = 'soimg'
    #  allowed_domains = ['https://image.so.com/']
    #  start_urls = ['http://https://image.so.com//']
    url = "https://image.so.com/zjl?ch=art&t1=196&sn=%s"
    start_urls = [url % 0]
    start_index = 0
    MAX_NUM = 1000

    def parse(self, response):
        json_dict = response.json()
        img_url_list = [li['qhimg_url'] for li in json_dict['list']]
        item = ImgItem()
        item['urls'] = img_url_list
        print(item)
        yield item

        #  self.start_index += json_dict['count']
        #  if json_dict['count'] > 0 and self.start_index < self.MAX_NUM:
        #      yield scrapy.Request(self.url % self.start_index)
