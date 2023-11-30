import scrapy

from ..items import PhotographyTipsScraperItem


class Website3Spider(scrapy.Spider):
    name = "website3"
    custom_settings = {
        'MONGODB_PIPELINE_SPIDER_NAME': name  # Pass the spider name to the pipeline
    }
    allowed_domains = ["expertphotography.com"]
    start_url = "https://expertphotography.com/archive/"

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
        # yield scrapy.Request(url=get_scrapeops_url(self.start_urls[0]), callback=self.parse)
        yield scrapy.Request(url=self.start_url, headers=headers, callback=self.parse_section)

    def parse_section(self, response):
        main = response.css('main.tmp-main')
        articles_urls = main.css('div.card a::attr(href)').getall()
        for url in articles_urls:
            headers = {'User-Agent': 'UserAgent'}
            yield scrapy.Request(url=url, headers=headers, callback=self.parse_article)

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            headers = {'User-Agent': 'UserAgent'}
            yield response.follow(next_page, headers=headers, callback=self.parse_section)

    def parse_article(self, response):
        url = response.url
        main = response.css('main article')
        title = main.css('header h1::text').get()

        content = main.css('div.entry-content').xpath('.//*//text()').getall()

        images = main.css('img::attr(src)').extract()

        tags = response.css('aside.sidebar nav').css('ul li a::text').extract()

        item = PhotographyTipsScraperItem()
        item['title'] = title
        item['content'] = content
        item['url'] = url
        item['images_url'] = images
        item['article_tags'] = tags
        # Yield the data for this article
        yield item

