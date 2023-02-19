from pathlib import Path
import requests
from random import randint
import scrapy

from tutorial.settings import SCRAPEOPS_API_KEY


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    SCRAPEOPS_API_KEY = '97d13fbd-22d5-4c93-aabb-799c1b622764'

    def start_requests(self):
        urls = [
            "http://httpbin.org/headers",
            "https://it.wethenew.com/it",
            "https://stockx.com/it-it",
            "https://www.klekt.com/seller/air-force-1-low-feel-free-lets-talk-2022?condition=new",
            "https://restocks.net/it",
            "https://hypeboost.com/it",
            "https://www.goat.com/"

        ]

        response = requests.get(
            url='https://headers.scrapeops.io/v1/browser-headers',
            params={
                'api_key': '97d13fbd-22d5-4c93-aabb-799c1b622764',
                'num_headers': '4'}
        )
        json_response = response.json()

        headers_list = json_response.get('result', [])
        random_index = randint(0, len(headers_list) - 1)
        headers = headers_list[random_index]

        for url in urls:

            yield scrapy.Request(url=url, callback=self.parse, headers=headers, meta={'handle_httpstatus_all': True})

    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = f'quotes-{page}.html'
        # Path(filename).write_bytes(response.body)
        #self.log(f'Saved file {filename}')
        print(response.url.split("/")[-2] + " :" + str(response.status))
