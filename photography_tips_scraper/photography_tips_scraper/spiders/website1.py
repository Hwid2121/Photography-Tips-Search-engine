from pathlib import Path
from urllib.parse import urlencode

import scrapy
import shadow_useragent

ua = shadow_useragent.ShadowUserAgent()

API_KEY = "1208de1b-9d3a-435f-a41c-df151ef7cfd1"


def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url, 'bypass': 'cloudflare'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class Website1Spider(scrapy.Spider):
    name = "website1"
    allowed_domains = ["www.dpreview.com"]
    start_urls = [
        "https://www.dpreview.com/features/photography?page=1",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=get_scrapeops_url(url), callback=self.parse)

    def parse(self, response):
        title =  response.css('h1::text').get()

        processed_data = {
            "title": title,
        }
        yield processed_data