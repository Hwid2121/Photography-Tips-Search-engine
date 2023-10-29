from pathlib import Path
from urllib.parse import urlencode

import scrapy

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
        # Find all article divs
        articles = response.css('div.article')

        for article in articles:
            # Extract the title from the current article
            title = article.css('div.content div.header div.title a::text').get()

            # Extract the content from the current article
            content = article.css('div.content div.body p::text').get()

            # Create a dictionary to store the extracted data for this article
            data = {
                'title': title,
                'content': content,
                'url': response.url,
            }

            # Yield the data for this article
            yield data