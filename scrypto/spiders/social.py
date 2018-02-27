# -*- coding: utf-8 -*-
import scrapy
#from selenium import webdriver
#sauver la liste des coins_names dans un fichier et faire un readlines dessus pour recréér un liste urls


class SocialSpider(scrapy.Spider):
    name = 'social'
    
    #for coin in coins:
    #    print('this is the number 2 list:  \n  ' + coin)
    #urls=list()

    #for name in range (len(coins)-1):
    #    add='https://coinmarketcap.com/currencies/' + coins[name] + '/#social/'
    #    urls.append(add)
        
    def start_requests(self):
        #allowed_domains = ["coinmarketcap.com"]
        #urls = ['https://coinmarketcap.com/currencies/' + name + '/']
        #urls=['http://coinmarketcap.com/currencies/dogecoin/#social',
        #      'http://coinmarketcap.com/currencies/siacoin/#social']
        urls = list()    
        filename='//var//www//scrypto//integration//scrypto//spiders//files//currencies.txt'
        with open (filename, 'r', encoding='utf-8') as fichier:
            var = fichier.read()
            coins = var.strip().split('\n')
            for element in coins:
            	url=f'https://coinmarketcap.com/currencies/{element}/#social'
    	        urls.append(url)
    	        print(url)
            print(urls)
        for a, url in enumerate(urls):
            yield scrapy.Request(url=url, callback=self.parse)
            print("i'm scraping my " , a , 'response!!!! \n')

    def parse(self, response):
        filename = "//var//www//scrypto//integration//scrypto//spiders//files//links.txt"
        with open(filename, 'a', encoding='utf-8') as fichier:
            selector=response.xpath('//div[@class="container"]/div[@class="row"]/div[@class="col-lg-10"]/div[@class="row bottom-margin-1x"]/div[@class="col-xs-12 tab-content"]/div[@class="tab-pane"]/div[@class="row"]/div[@class="col-sm-6 text-left"]/a/@href').extract()[0]
            #Getting data variable in result
            coin = selector[20:]
            fichier.write(coin + "\n")

