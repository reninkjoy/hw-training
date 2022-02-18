# import scrapy
# import re
# import requests
# import json
# import subprocess
# import string
# import gzip
# from io import StringIO
# import io
# from scrapy import signals
# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from scrapy.http import Request, FormRequest
# from xml.dom import minidom
# from pymongo import MongoClient
# from haraj.proxy import parse_proxy
# from datetime import datetime
# from haraj.settings import *
# # from databasenotifier import automation_script
# from haraj.items import *
# import itertools
# headers = {
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "access-control-request-headers": "trackid",
#     "access-control-request-method": "POST",
#     "origin": "https://haraj.com.sa",
#     "referer": "https://haraj.com.sa/",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"
# }
# class HarajSpider(scrapy.Spider):
#     db = MongoClient('mongodb://localhost:27017')[dbname]
#     name = 'haraj'
#     allowed_domains = ['haraj.com.sa']
#
#     def start_requests(self):
#             query = {"query":"query($tag:String,$page:Int) { posts( tag:$tag, page:$page) {\n\t\titems {\n\t\t\tid status authorUsername title city postDate updateDate hasImage thumbURL authorId\n\t\t}\n\t\tpageInfo {\n\t\t\thasNextPage\n\t\t}\n\t\t} }","variables":{"tag":"حراج العقار","page":1}}
#             url = "https://graphql.haraj.com.sa/?queryName=detailsPosts_tag_page1"
#             meta={"page":1}
#             yield Request(url, callback=self.parse_search, method="POST", meta=meta,body=json.dumps(query),dont_filter=True,headers=headers)
#
#     def parse_search(self,response):
#         meta=response.meta
#         base_url="https://haraj.com.sa/"
#         dic=json.loads(response.text)
#         data=dic['data']
#         posts=data['posts']
#         items=posts['items']
#         if items:
#             for id in items:
#                 title=id['title'].replace(" ","_")
#                 urls=base_url+"11"+str(id["id"])+"/"+str(title)
#                 item=HarajUrlItem(
#                     url=urls
#                 )
#                 yield(item)
#             meta = {"page": meta['page'] + 1}
#             query = {
#                 "query": "query($tag:String,$page:Int) { posts( tag:$tag, page:$page) {\n\t\titems {\n\t\t\tid status authorUsername title city postDate updateDate hasImage thumbURL authorId\n\t\t}\n\t\tpageInfo {\n\t\t\thasNextPage\n\t\t}\n\t\t} }",
#                 "variables": {"tag": "حراج العقار", "page":meta['page']+1}}
#             url = "https://graphql.haraj.com.sa/?queryName=detailsPosts_tag_page"+str(meta['page']+1)
#
#             yield Request(url, callback=self.parse_search, method="POST", meta=meta, body=json.dumps(query), dont_filter=True,
#                           headers=headers)
