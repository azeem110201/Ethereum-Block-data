import scrapy
import time

BASE_URL = 'https://explorer-web.api.btc.com/v1/eth/blocks?page={}&size=150'
class EthSpider(scrapy.Spider):
    name = 'eth'
    start_urls = [
        BASE_URL.format(1)
    ]
    pageNum = 2

    def parse(self, response):
        data = response.json()
        
        for i in range(len(data['data']['list'])):
            yield data['data']['list'][i]

        next_page = 'https://explorer-web.api.btc.com/v1/eth/blocks?page=' + str(EthSpider.pageNum) + '&size=150'

        time.sleep(0.2)

        # if EthSpider.pageNum <= 1000:     // this will scrape 150000 eth block data in around 10-12 mins the below if statement takes hours to scrape the data so beware will running
        if EthSpider.pageNum <= data['data']['page']:
            EthSpider.pageNum += 1
            yield response.follow(next_page, callback=self.parse)  
