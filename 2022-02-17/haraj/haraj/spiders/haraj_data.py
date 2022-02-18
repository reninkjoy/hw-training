import json
from scrapy.http import Request, FormRequest
from pymongo import MongoClient
from haraj.settings import *
from haraj.items import *
import datetime
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "access-control-request-headers": "trackid",
    "access-control-request-method": "POST",
    "origin": "https://haraj.com.sa",
    "referer": "https://haraj.com.sa/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"}

class HarajSpider(scrapy.Spider):
    name = 'haraj'
    allowed_domains = ['haraj.com.sa']

    def start_requests(self):
        with open('urls.json','r') as fp:
            data=fp.read()
        data=data.split("\n")
        item = {}
        for i in data:
            i=json.loads(i)
            url=i['url']
            item['url']=url
            yield Request(url, callback=self.parse_userid, meta=item, method="GET", headers=headers)
    def parse_userid(self,response):
        if response.status==200:
            meta=response.meta
            user_id=''.join(response.xpath('//span[@class="author"]/parent::a/@href').extract())
            user_id=user_id.split("/")
            meta['user_id'] = user_id[-1]
            id=meta['url']
            id=id.split('/')[-2]
            id=int(id[2:])
            meta['id']=id
            url = "https://graphql.haraj.com.sa/?queryName=postLikeInfo,postContact"
            query={"query":"query postLikeInfo_postContact($id: Int!, $token: String,$postId: Int!) {\n\t\t\n\t\tpostLikeInfo(id: $id, token: $token)\n\t\t{ \n                    isLike\n                    total\n                    isFollowing\n                     }\n\t\n\r\n\t\tpostContact(postId: $postId)\n\t\t{ \n                    contactText\n                    contactMobile\n                     }\n\t\n\t}","variables":{"id":id,"token":"","postId":id}}
            yield Request(url, callback=self.parse_phone,meta=meta, method="POST", body=json.dumps(query),dont_filter=True, headers=headers)
        else:
            print("Error in response status: ",response.url,response.status)
    def parse_phone(self,response):
        meta=response.meta
        dic = json.loads(response.text)
        data = dic['data']
        posts = data['postContact']
        meta['phone_number']=posts['contactMobile']
        url = "https://graphql.haraj.com.sa/?queryName=detailsPosts_singlePost"
        query={"query": "query($ids:[Int]) { posts( id:$ids) {\n\t\titems {\n\t\t\tid status authorUsername title city postDate updateDate hasImage thumbURL authorId bodyTEXT city tags imagesList commentStatus commentCount upRank downRank geoHash\n\t\t}\n\t\tpageInfo {\n\t\t\thasNextPage\n\t\t}\n\t\t} }",
                "variables": {"ids": [meta['id']]}}
        yield Request(url, callback=self.parse_search,meta=meta, method="POST", body=json.dumps(query),dont_filter=True, headers=headers)

    def parse_search(self,response):
        meta=response.meta
        dic = json.loads(response.text)
        data=dic['data']
        posts=data['posts']
        items=posts['items']
        nowdate = datetime.datetime.now().date()
        for item in items:
            broker_display_name=item['authorUsername']
            broker=broker_display_name.upper()
            category_url="/tags/حراج%20العقار"
            title = item['title']
            description=item['bodyTEXT'].replace("\n",'').replace("\r","").replace("\t","").replace("\\","").replace("'","").replace(",","").strip()
            location=item['city']
            nowdate=datetime.datetime.now().date()
            scraped_ts=nowdate.strftime("%Y_%m_%d")
            number_of_photos=len(item["imagesList"])
            date=nowdate.strftime("%Y_%m_%d")
            iteration_number=nowdate.strftime("%Y_%m")
        item =  HarajItem(id= meta['id'],
                url= meta['url'],
                broker_display_name= broker_display_name,
                broker= broker,
                category= '',
                category_url= category_url,
                title= title,
                property_type= '',
                depth=  '',
                sub_category_1= '',
                sub_category_2='',
                description=description,
                location=location,
                price='',
                currency='',
                price_per= '',
                bedrooms= '',
                bathrooms= '',
                furnished= '',
                rera_permit_number='',
                dtcm_licence='',
                scraped_ts=scraped_ts,
                amenities= '',
                details= '',
                agent_name= '',
                number_of_photos= number_of_photos,
                reference_number= '',
                user_id= meta["user_id"],
                phone_number= meta['phone_number'],
                date= date,
                iteration_number= iteration_number,
                latitude ='',
                longitude= '')
        yield item



