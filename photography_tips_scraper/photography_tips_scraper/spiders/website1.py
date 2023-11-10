import scrapy
from urllib.parse import urlencode

API_KEY = "1208de1b-9d3a-435f-a41c-df151ef7cfd1"


def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url, 'bypass': 'cloudflare'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class Website1Spider(scrapy.Spider):
    name = "website1"
    allowed_domains = ["www.dpreview.com"]
    # start_urls = ["https://www.dpreview.com/features/photography"]

    start_url = 'https://www.dpreview.com/features'

    def parse_start_urls(self, response):
        # Find all the urls of each section of articles
        sections = response.css('div.sampleArticles')

        for section in sections:
            url = section.css('div.category div.articlesCount a::attr(href)').get()
            section_url = response.urljoin(url)
            headers = {'User-Agent': 'UserAgent'}
            # go inside the url of the article
            yield scrapy.Request(url=section_url, headers=headers, callback=self.parse)

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
        # yield scrapy.Request(url=get_scrapeops_url(self.start_urls[0]), callback=self.parse)
        yield scrapy.Request(url=self.start_url, headers=headers, callback=self.parse_start_urls)

    def parse_article(self, response):
        # Extract the title from the current article
        title = response.css('div.articleHeader h1::text').get()

        # Extract the content from the current article
        main_content = response.css('div.mainContent div.articleBody')

        content = main_content.xpath('.//p/text() | .//h2/text()').getall()
        data = {
            'title': title,
            'content': content,
            'url': response.url,
        }

        # Yield the data for this article
        yield data

    def parse(self, response):
        # Find all article divs
        articles = response.css('div.article')

        for article in articles:

            url = article.css('div.content div.header div.title a::attr(href)').get()
            # output the url of the article

            article_url = response.urljoin(url)
            headers = {'User-Agent': 'UserAgent'}
            # go inside the url of the article
            yield scrapy.Request(url=article_url, headers=headers, callback=self.parse_article)


        # Extract the next page URL
        next_page = response.css('td.next.enabled a::attr(href)').get()

        # If there's a next page, follow the link and continue scraping
        if next_page:
            # Construct the absolute URL without involving the ScrapeOps proxy
            next_page_url = response.urljoin(next_page)
            headers = {'User-Agent': 'UserAgent'}
            yield scrapy.Request(url=next_page_url, headers=headers, callback=self.parse)





# fix link in the articles that are not linked well
# fix the regex for the p for get the text clean and get the text from all the tags inside (a, b, strong, etc)

