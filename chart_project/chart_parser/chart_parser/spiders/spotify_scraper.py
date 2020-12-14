import scrapy

from ..items import ChartParserItem


class SpotifyScraperSpider(scrapy.Spider):
    name = 'spotify_scraper'
    allowed_domains = ['spotifycharts.com']
    start_urls = ['https://spotifycharts.com/regional']

    def parse(self, response):
        item = ChartParserItem()
        item['author'] = response.xpath('//td[@class="chart-table-track"]/span/text()').extract()
        item['song'] = response.xpath('//td[@class="chart-table-track"]/strong/text()').extract()
        item['position'] = response.xpath('//td[@class="chart-table-position"]/text()').extract()
        return item

