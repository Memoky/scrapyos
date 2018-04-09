from scrapy.spiders import Spider


class BlogSpider(Spider):
    name = 'test1'
    start_urls = ['https://www.memoky.cc/']

    def parse(self, response):
        titles = response.xpath(
            '//head/title/text()').extract()
        for title in titles:
            print title
# ssadasdsaSas
