from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from spiders.currencies import CurrencySpider
from spiders.social import SocialSpider
#from spiders.twitter import TweetSpider
#import threading
#import os
 
configure_logging()
runner = CrawlerRunner()
#process = CrawlerProcess(get_project_settings())

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CurrencySpider)
    yield runner.crawl(SocialSpider)
    #yield runner.crawl(TweetSpider)


crawl()

#runner.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the last crawl call is finished

#process.start(stop_after_crawl=False)