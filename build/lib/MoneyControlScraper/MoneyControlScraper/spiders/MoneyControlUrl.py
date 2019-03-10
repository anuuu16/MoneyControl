# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from MoneyControlScraper.items import MoneycontrolscraperItem 
import redis
from scrapy.conf import settings
from bs4 import BeautifulSoup
import pymongo
import pprint
from bson.objectid import ObjectId
from bs4 import BeautifulSoup
from requests import get
import re
import requests
#RUN COMMAND
#activate SearchEngine
#cd SearchEngineResources/MoneyControlScraper/MoneyControlScraper
#scrapy crawl UrlScrapper -o links.csv -t csv
class MoneyControlUrlScrapper(CrawlSpider):
    # The name of the spider
    name = "UrlScrapper"

    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ["moneycontrol.com"]

    # The URLs to start with
    start_urls = ["https://www.moneycontrol.com/"]

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    redis_host = settings["REDIS_SERVER"]
    redis_port = settings["REDIS_PORT"]
    redis_urlset = settings["REDIS_URLSET"]
    redis_contentSet=settings["REDIS_CONTENTSET"]
    redis_errorSet=settings["REDIS_ERRORSET"]
    
    r = redis.Redis(
                host=redis_host,
                port=redis_port)

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items
    def parse_items(self, response):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # The list of items that are found on the particular page
        items = []
        link=response.url
        print(link)
        if not self.r.sismember(self.redis_urlset, str(link)):
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link:
                    is_allowed = True
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                print("parsing..............")
                html_soup = BeautifulSoup(response.body, 'lxml')
                # kill all script and style elements
                for script in html_soup(["script", "style"]):
                    script.extract()    # rip it out
                item = MoneycontrolscraperItem()
                item['content']=html_soup.get_text()
                if(html_soup.title is not None):
                    item['title']=html_soup.title.string
                else:
                    item['title']=""
                for tag in html_soup.head.find_all("meta"):
                    if tag.get("name", None) == "description" or tag.get("name", None) == "twitter:description":
                        item['description']=tag.get("content", None)
                    if tag.get("name", None) == "keyword":
                        item['keyword']=tag.get("content", None)
                item['url']= link
                items.append(item)
                self.r.sadd(self.redis_urlset, str(link))
            else:
                self.r.sadd(self.redis_errorSet, str(link))
        # Return all the found items
        print("+++++++++++++++++=========================================================")
        return items