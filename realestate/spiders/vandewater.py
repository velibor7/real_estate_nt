import scrapy
from ..items import RealestateItem


class VandewaterSpider(scrapy.Spider):
    name = 'vandewater'
    start_urls = ['https://vandewatergroep.nl/bestaande-woningen/#q1bKzs8vyCgtLVKyAjOVdMBUQVFmVrGSVbVSbmIFUMbI3NTAwECpVkcpvygltSipEihWXJJYUlpslVicrFQLAA/']

    def parse(self, response):
        for href in response.xpath('//*[(@id = "entity-items")]//*[contains(@class, "overlay")]/@href'):
            url = response.urljoin(href.get())
            print(f"Scraping url: {url}")
            yield scrapy.Request(url, callback=self.parse_item)

    
    def parse_item(self, response):
        item = RealestateItem()
        print(f"Item keys: {item.fields}")
        item['title'] = response.xpath('//h1/text()').get()

        for row in response.xpath('//div[contains(@class, "container")]//li[contains(@class, "clearfix")]'):
            key = row.xpath('./strong//text()').get().lower().replace(' ', '_')
            val = row.xpath('./span//text()').get()

            # adding just the items we defined we want in items
            for k in item.fields:
                # print(f"Key in second loop: {k}")
                if key == k:
                    item[key] = val
        yield item