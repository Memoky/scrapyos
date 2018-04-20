# coding:utf-8
from scrapy.spiders import Spider
from scrapyos.items import WorldCupItem
from scrapy import Request


class DoubanMovieTop250Spider(Spider):
    name = 'wc_2018'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://sports.sina.com.cn/g/laliga/2017-12-02/doc-ifypikwt2402715.shtml'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = WorldCupItem()

    def parse(self, response):
        item = WorldCupItem()
        matchs = response.xpath(
            '//div[@class="article-a__content"]/table/tbody/tr')
        for match in matchs[2:]:
            matchinfo = match.xpath(".//td/text()").extract()
            item['time'] = matchinfo[0]
            item['fieldorder'] = matchinfo[1]
            item['match'] = matchinfo[2]
            item['city'] = matchinfo[3]
            yield item
        # for movie in movies:
        #     item['ranking'] = movie.xpath(
        #         './/div[@class="pic"]/em/text()').extract()[0]
        #     item['movie_name'] = movie.xpath(
        #         './/div[@class="hd"]/a/span[1]/text()').extract()[0]
        #     item['score'] = movie.xpath(
        #         './/div[@class="star"]/span[@class="rating_num"]/text()'
        #     ).extract()[0]
        #     item['score_num'] = movie.xpath(
        #         './/div[@class="star"]/span/text()').re(ur'(\d+)人评价')[0]  # aaa
        #     yield item

        # next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        # if next_url:
        #     next_url = 'https://movie.douban.com/top250' + next_url[0]
        #     yield Request(next_url, headers=self.headers)
