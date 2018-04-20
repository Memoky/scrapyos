# coding:utf-8
from scrapy.spiders import Spider
from scrapyos.items import WorldCupItem
from scrapy import Request


class WorldCup(Spider):
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
