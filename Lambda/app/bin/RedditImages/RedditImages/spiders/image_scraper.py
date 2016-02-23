# -*- coding: utf-8 -*-
import scrapy
from RedditImages.items import RedditImagesItem


class ImageScraperSpider(scrapy.Spider):
    name = "image_scraper"
    allowed_domains = ["www.reddit.com"]
    start_urls = (
        'http://www.reddit.com/',
    )

    def parse(self, response):
        # imgExtentions = ['.jpeg', '.jpg', '.png', '.gif', '.svg']
        for sel in response.xpath('//*[@id="siteTable"]/div'):
            item = RedditImagesItem()
            item['title'] = sel.xpath('div[2]/p[1]/a/text()').extract()
            item['url'] = sel.xpath('div[2]/p[1]/a/@href').extract()
            item['image'] = sel.xpath('a[1]/img/@src').extract()
            yield item
