from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from RedditImages.spiders.image_scraper import ImageScraperSpider
from scrapy.utils.project import get_project_settings

spider = ImageScraperSpider(domain='reddit.com')
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
log.msg('Reactor activated...')
reactor.run()
log.msg('Reactor terminated.')
