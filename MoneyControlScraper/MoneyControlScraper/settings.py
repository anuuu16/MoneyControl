# -*- coding: utf-8 -*-

# Scrapy settings for MoneyControlScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MoneyControlScraper'

SPIDER_MODULES = ['MoneyControlScraper.spiders']
NEWSPIDER_MODULE = 'MoneyControlScraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MoneyControlScraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'MoneyControlScraper.middlewares.MoneycontrolscraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'MoneyControlScraper.middlewares.MoneycontrolscraperDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'MoneyControlScraper.pipelines.ElasticSearchPipeline' : 300,
    'MoneyControlScraper.pipelines.MoneycontrolscraperPipeline': 400
}

ELASTICSEARCH_SERVER = 'localhost' 
ELASTICSEARCH_PORT = 9200 
ELASTICSEARCH_INDEX = 'moneycontrolone'
ELASTICSEARCH_TYPE = 'htmlcontent'
ELASTICSEARCH_UNIQ_KEY = 'url'

#ITEM_PIPELINES = ['MoneyControlScraper.pipelines.MoneycontrolscraperPipeline' ]
# MONGODB_SERVER = "ds061474.mlab.com"
# MONGODB_PORT = 61474
# MONGODB_DB = "moneycontrol"
# MONGODB_COLLECTION = "MoneyControlContent"
# MONGODB_USER = "admin"
# MONGODB_PASS = "Kratos@123"
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "SearchEngine"
MONGODB_COLLECTION = "moneycontrolone"

REDIS_SERVER = "localhost"
REDIS_PORT = 6379
# Redis set for storing urls
REDIS_URLSET = "urlset"
REDIS_CONTENTSET = "conset"
REDIS_ERRORSET = "errset"
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_ENABLED = False