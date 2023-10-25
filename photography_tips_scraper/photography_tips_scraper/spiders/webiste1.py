from pathlib import Path

import scrapy


class Website1Spider(scrapy.Spider):
    name = "website1"

    def start_requests(self):
        urls = [
            "https://www.dpreview.com/features/photography?page=1",
             "https://www.dpreview.com/features/photography?page=2"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")