import scrapy
from maoyanSpiders.items import MaoyanspidersItem
from lxml import etree

class MaospiderSpider(scrapy.Spider):
    name = 'maoSpider'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/'] 
     
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        
        yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        self.items = []
        html = etree.HTML(response.text)
        dls = html.xpath('//*/dd')    
        for dl in dls:
            name = dl.xpath(
                './div[1]/div[2]/a/div/div[1]/span/text()')[0]
            item_type = dl.xpath(
                './div[1]/div[2]/a/div/div[2]/text()')[1].strip()
            time = dl.xpath(
                './div[1]/div[2]/a/div/div[4]/text()')[1].strip()
         
            item = MaoyanspidersItem()
            item["name"] = name
            print(name)
            item["item_type"] = item_type
            print(item_type)
            item["time"] = time
            print(time)          
            yield item
        