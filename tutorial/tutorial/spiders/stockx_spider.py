import scrapy
from pathlib import Path


class StockxSpider(scrapy.Spider):
    name = "stockx"

    def start_requests(self):

        shoes = ["air-jordan-1-retro-ajko-low-sp-union"]
        baseUrl = "https://stockx.com/it-it/"
        url = "http://httpbin.org/headers"

        for shoe in shoes:
            #url = baseUrl + shoe
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
        print(response.url.split("/")[-2] + " :" + str(response.status))
