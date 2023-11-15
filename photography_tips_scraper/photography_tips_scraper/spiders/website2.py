import scrapy


class Website2Spider(scrapy.Spider):
    name = "website2"
    allowed_domains = ["photographylife.com"]

    start_url = 'https://photographylife.com/learn-photography'

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
        # yield scrapy.Request(url=get_scrapeops_url(self.start_urls[0]), callback=self.parse)
        yield scrapy.Request(url=self.start_url, headers=headers, callback=self.parse)

    def parse(self, response):

        main_content = response.css('div.entry-content ')
        ul_content = main_content.css('ul')
        headers = {'User-Agent': 'UserAgent'}

        url = 'https://photographylife.com/how-was-this-picture-made-12'
        yield scrapy.Request(url=url, headers=headers, callback=self.parse_article)

        #
        # for ul_content in ul_content:
        #     lis = ul_content.css('li')
        #     for li in lis:
        #         url = li.css('a::attr(href)').get()
        #         url = response.urljoin(url)
        #         headers = {'User-Agent': 'UserAgent'}
        #         # go inside the url of the article
        #         yield scrapy.Request(url=url, headers=headers, callback=self.parse_article)

    def parse_article(self, response):
        content_head = response.css('header.entry-header')
        content_body = response.css('div.entry-content')
        content_footer = response.css('div.entry-footer')
        title = content_head.css('h1.entry-title::text').get()

        content = content_body.xpath('.//*//text()').getall()
        # extracting images src
        images = content_body.css('img::attr(src)').extract()
        # extracting tags
        tags = content_footer.css('span.entry-tags a::text').extract()

        print("title", title)
        print("content", content)
        print("images", images)
        print("tags", tags)
        print("url", response.url)
        print("--------------------------------------------------")



