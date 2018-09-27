# -*- coding: utf-8 -*-
import scrapy
import json

class SpJobSpider(scrapy.Spider):
    name = 'sp_job'
    allowed_domains = ['zhilian.com']
    # start_urls = ['http://zhilian.com/']
    raw_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=801'
                  '&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=2'
                  '&kw=python&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:'
                  '%22801%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D']

    def parse(self, response):
        resp_data = json.loads(response.text)
        for job in resp_data['data']['results']:
            url = job['positionURL']
            return
        # pass
