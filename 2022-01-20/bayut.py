headers={
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
 	"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
	"cache-control": "max-age=0",
	"cookie": "anonymous_session_id=3ac75148-f229-4b2e-91db-58d58a8ee62f; device_id=kyitdktvn0zun7o78; os_name=N%2FA; os_version=N%2FA; browser_name=N%2FA; browser_version=N%2FA; settings=%7B%22area%22%3Anull%2C%22currency%22%3A%22AED%22%2C%22installBanner%22%3Atrue%2C%22searchHitsLayout%22%3A%22LIST%22%7D; abTests=%7B%22MobileChatButton%22%3A%22original%22%2C%22EmailAlertsBanners%22%3A%22original%22%2C%22SearchPageListingCard%22%3A%22original%22%2C%22CompactNavBar%22%3A%22original%22%7D; banners=%7B%7D; userLocation=%7B%22countryCode%22%3Anull%2C%22countryName%22%3Anull%2C%22cityName%22%3Anull%7D; userGeoLocation=%7B%22coordinates%22%3Anull%2C%22closestLocation%22%3Anull%2C%22loading%22%3Afalse%2C%22error%22%3Anull%7D; PHPSESSID=688h0fdcnh041tstsp57v1v2v4; TRUCHECK_ACKNOWLEDGED=true; AWSALB=N34Y1BG+2bbemwh3kkNXz9F8J0kNkiY7/ZQ9zXHWgk9EMujZMJaQzMUgZ+YBpMXH3jTvkcyBpn1yuB1dFjLZrTpCOfQQaZjioTOJjn9HDwW2xfT434UFCwzNGJV9; AWSALBCORS=N34Y1BG+2bbemwh3kkNXz9F8J0kNkiY7/ZQ9zXHWgk9EMujZMJaQzMUgZ+YBpMXH3jTvkcyBpn1yuB1dFjLZrTpCOfQQaZjioTOJjn9HDwW2xfT434UFCwzNGJV9; XSRF-TOKEN=eyJpdiI6IlwvbEJNTGFOa3Z1bjFKZFZMODdIc0xnPT0iLCJ2YWx1ZSI6IlZPZDRnaWZPSGV0TFlaXC9HaFRqNExCNDBrTDlBWFY2RWpcL3h4dm95ZmRGWU5LV1poSHY0aEpIVFpORFIwUFpvanpNa0lqNTRTTGZpZlNkTmg3dXBJZmc9PSIsIm1hYyI6ImZkOTYwMjBhODZhMGFlOTFmNmQzOTY4MjVmNWZiYzY5MDNmYTEwMDUwZDA2YTRlM2RmM2Y5MDUyYTQ4OWE1NDUifQ%3D%3D; byt_session=eyJpdiI6ImxEWTVJRXR2OUQxaENFc0tpNHhreFE9PSIsInZhbHVlIjoiYmZlWkNEMWVjM1BqaTUxdDB0MWhoazl5emNPWk54ZHE2eFBBRm9OOTVXRkQyWDcwRnJ1VXR4QzZSOEhcL1pOXC8rNEFORVwvWjVINmc0VENPbnN1dWxtNWc9PSIsIm1hYyI6IjRlMjVhM2YxMjM3NGE1NGIyN2IyNWNlMWZlZmUxYzE4OTU2ZGNhMjEyYmVjMDY5ZjlmODgzODJlOWY0MjdlMTEifQ%3D%3D; landing_url=%2Fto-rent%2Fproperty%2Fdubai%2F",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "none",
	"sec-fetch-user": "?1",
	"sec-gpc":"1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

import requests
import json 
from lxml import html
import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()
db=client.bayut

urls="https://www.bayut.com/to-rent/property/dubai/"

base_url="https://www.bayut.com"

property_id="//span[@aria-label='Reference']/text()"
purpose="//span[@aria-label='Purpose']/text()"
types="//span[@aria-label='Type']/text()"
added_on="//span[@aria-label='Reactivated date']/text()"
furnishing="//span[@aria-label='Furnishing']/text()"
currency="//span[@aria-label='Currency']/text()"
amount="//span[@aria-label='Price']/text()"
location="//div[@aria-label='Property header']/text()"
bedrooms="//span[@class='fc2d1086']/text()"
bathrooms="//span[@class='fc2d1086']/text()"
size="//span[@class='fc2d1086']//span/text()"
permit_number="//div[@class='_74093213']//span/text()"
agent_name="//span[@class='_55e4cba0']/text()"
image_url="//img[@src][@aria-label='Cover photo']/@src"
breadcrumbs="//span[@class='_327a3afc']/text()"
amenities="//span[@class='_005a682a']/text()"
description="//span[@class='_2a806e1e']/text()"

def data(url):

	page = requests.get(url = url, headers = headers)
	response = html.fromstring(page.content)

	bproperty_id=" ".join(response.xpath(property_id))
	bpurpose=" ".join(response.xpath(purpose))
	btypes=" ".join(response.xpath(types))
	badded_on=" ".join(response.xpath(added_on))
	bfurnishing=" ".join(response.xpath(furnishing))
	bcurrency=" ".join(response.xpath(currency))
	bamount=" ".join(response.xpath(amount))
	blocation=" ".join(response.xpath(location))
	bbedrooms=" ".join(response.xpath(bedrooms))
	bbathrooms=" ".join(response.xpath(bathrooms)[1])
	bsize=" ".join(response.xpath(size))
	bpermit_number=int(response.xpath(permit_number)[-1])
	bagent_name=" ".join(response.xpath(agent_name))
	bimage_url=" ".join(response.xpath(image_url))
	bbreadcrumbs=">".join(response.xpath(breadcrumbs))
	bamenities=" ".join(response.xpath(amenities))	
	bdescription=" ".join(response.xpath(description))	

	item = {}
	item['property_id'] = bproperty_id
	item['purpose'] = bpurpose
	item['types'] = btypes
	item['added_on'] = badded_on
	item['furnishing'] =bfurnishing
	item['price'] = {"currency":bcurrency,"amount":bamount}
	item['location'] = blocation
	item['bed_bath_size'] = {"bedrooms":bbedrooms,"bathrooms":bbathrooms,"size":bsize}
	item['permit_number'] = bpermit_number
	item['agent_name'] = bagent_name
	item['image_url'] = bimage_url
	item['breadcrumbs'] = bbreadcrumbs
	item['amenities'] = bamenities
	item['description'] = bdescription

	post=db.login.insert_one(item)
	# details=json.dumps(item)
	# with open("outs.json","a") as f:
	# 	f.write(json.dumps(json.loads(details),indent=4))

def links(pages):
	try :
		page = requests.get(url = pages, headers = headers)
		response = html.fromstring(page.content)
		links = response.xpath('//a[@aria-label="Listing link"]/@href')
		for link in links:
		    print(link)
		    data(base_url+link)

	except :
		continue

try :
	while True:
		page = requests.get(url = urls, headers = headers)
		response = html.fromstring(page.content)
		linkss="".join(response.xpath('//a[@title="Next"]/@href'))
		links(base_url+linkss)
		print(base_url+linkss)
		urls=base_url+linkss
except :
	print("END")