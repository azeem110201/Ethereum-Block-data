BOT_NAME = 'ethereum'

SPIDER_MODULES = ['ethereum.spiders']
NEWSPIDER_MODULE = 'ethereum.spiders'

# PROXY_POOL_ENABLED = True

ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}