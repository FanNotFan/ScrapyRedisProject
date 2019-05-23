#!/usr/bin/env python
# encoding: utf-8
'''
@author: lennon
@license: (C) Copyright 2019-2020, Node Supply Chain Manager Corporation Limited.
@contact: v-lefan@expedia.com
@software: pycharm
@file: jobbole.py
@time: 2019-05-22 18:53
@desc:
'''

from scrapy_redis.spiders import RedisSpider

class JobboleSpider(RedisSpider):
    name = 'jobbole'
    redis_key = 'jobbole:start_urls'
    allowed_domains = ['www.jobbole.com']

    def parse(self, response):
        # do stuff
        pass