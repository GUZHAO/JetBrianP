import scrapy
from scrapy.item import Item, Field
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class StackSpider(Spider):
    name = "stack"
    start_urls = [
        "http://www.totalwine.com/spirits/gin/c/000870?storename=1701,1702,1703,1704,1502,1504,1503,1501,303,302&sort=name-asc"
    ]

    def parse(self, response):
        alreadyhave = Selector(response).xpath('//div[@class="plp-product-desc-wrap"]')

        # for question in alreadyhave:
        #     #item = StackItem()
        #     yield{'name': alreadyhave.xpath(
        #         'a[@class="analyticsProductName"]/text()').extract()
        #     }
            # item['url'] = alreadyhave.xpath(
            #     'a[@class="analyticsProductName"]/@href').extract()[0]
            # item['quantity'] = alreadyhave.xpath(
            #     '//div[@class="plp-product-qty"]/text()').extract()[0]
            # item['price'] = alreadyhave.xpath(
            #     '//div[@class="plp-product-buy-price-mix"]/text()').extract()[0]
            #yield item