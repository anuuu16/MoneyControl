# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import json
import requests
from elasticsearch import Elasticsearch

class MoneycontrolscraperPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
            connection = pymongo.MongoClient(
                settings['MONGODB_SERVER'],
                settings['MONGODB_PORT']
            )
            db = connection[settings['MONGODB_DB']]
            self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Url added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
            print("mongo db saved")
        return item

class ElasticSearchPipeline(object):
    def __init__(self):
            self.es = Elasticsearch([{'host': settings['ELASTICSEARCH_SERVER'], 'port': settings['ELASTICSEARCH_PORT']}])
            self.es_index =settings['ELASTICSEARCH_INDEX']
            self.es_type =settings['ELASTICSEARCH_TYPE']
            self.es_unique_key =settings['ELASTICSEARCH_UNIQ_KEY']

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.es.index(index=self.es_index, doc_type=self.es_type, id=item[self.es_unique_key], body=dict(item))
            log.msg("Url added to ElasticSearch database!",
                    level=log.DEBUG, spider=spider)
            print("es db saved")
        return item 

# class ElasticSearchPipeline(object):
# # def process_item(self, item, spider):
#     #     return item
#     def __init__(self):
#         #self.es = Elasticsearch([{'host': settings['ELASTICSEARCH_SERVER'], 'port': settings['ELASTICSEARCH_PORT']}])
#         self.es_index =settings['ELASTICSEARCH_INDEX']
#         self.es_type =settings['ELASTICSEARCH_TYPE']
#         self.es_unique_key =settings['ELASTICSEARCH_UNIQ_KEY']
#         #basic_auth = {'username': self.settings['ELASTICSEARCH_USERNAME'], 'password': self.settings['ELASTICSEARCH_PASSWORD']}
#         if settings['ELASTICSEARCH_PORT']:
#             uri = "%s:%d" % (settings['ELASTICSEARCH_SERVER'], settings['ELASTICSEARCH_PORT'])
#         else:
#             uri = "%s" % (settings['ELASTICSEARCH_SERVER'])

#         # self.es = ES([uri], basic_auth=basic_auth)
#         self.es = ES([uri])

#     def process_item(self, item, spider):
#         valid = True
#         for data in item:
#             if not data:
#                 valid = False
#                 raise DropItem("Missing {0}!".format(data))
#         if valid:
#             self.es.index(dict(item), self.es_index, self.es_type,
#                           id=item[self.es_unique_key], op_type='create',)
#             # log.msg("Url added to ElasticSearch database!",
#             #         level=log.DEBUG, spider=spider)
#         return item 