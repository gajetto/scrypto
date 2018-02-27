# -*- coding: utf-8 -*-
import scrapy

coins=list()

class CurrencySpider(scrapy.Spider):
    name = 'currencies'

    def start_requests(self):
    	#allowed_domains = ["coinmarketcap.com"]
        url = 'https://coinmarketcap.com/all/views/all'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = "//var//www//scrypto//integration//scrypto//spiders//files//currencies.txt"
        with open(filename, 'w', encoding='utf-8') as fichier:
            token = response.css('tr').xpath('@id').extract()
            coins = token[:320]
            for coin in coins:
                name=coin.strip().split("id-")[1]
                coins.append(name)
                fichier.write(f'{name} \n')
        return coins

#currency_spider=CurrencySpider()
#coins=currency_spider.parse(response)
for coin in coins:
    print('this is the number 1 list:  \n  ' + coin)
