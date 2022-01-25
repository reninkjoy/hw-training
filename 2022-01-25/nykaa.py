item={}
import datetime
import json


#product_name
product_name=response.xpath('//h1/text()').extract_first()
item["product_name"]=product_name

#Ratings
ratings=response.xpath('//div[@itemprop="aggregateRating"]/preceding-sibling::div/text()').extract()
ratings=float(ratings[0])/float(ratings[1].replace("/",""))
print(type(ratings))
item["ratings"]=ratings

#NO of Ratings
no_of_rating=response.xpath('//div[@itemprop="aggregateRating"]/following::div[2]/text()').extract_first()
item["no_of_rating"]=float(no_of_rating)

#No Of Review
no_of_review=response.xpath('//div[@itemprop="aggregateRating"]/following::div[4]/text()').extract_first()
item["no_of_review"]=float(no_of_review)

#MRP
mrp=response.xpath('//span[text()="MRP:"]/following-sibling::span/text()').extract_first("no value")
item["mrp"]=float(mrp.replace("₹",""))

#Expiry_date
expiry_date=response.xpath("//script[contains(text(),'expiry')]/text()").extract_first()
expiry_date=expiry_date.split(",")
expiry_date= ["{"+s+"}" for s in expiry_date  if "expiry" in s]
expiry_date = json.loads(str(expiry_date[-1]))
expiry_date=datetime.datetime.strptime(expiry_date['expiry'], '%d %B %Y').strftime('%Y/%m/%d')
item["expiry_date"]=expiry_date

#Country_of_Origin
country_of_origin=response.xpath("//script[contains(text(),'originOfCountryName')]/text()").extract_first()
country_of_origin=country_of_origin.split(",")
country_of_origin= ["{"+s+"}" for s in country_of_origin  if "originOfCountryName" in s]
country_of_origin = json.loads(str(country_of_origin[-1]))
item["country_of_origin"]=country_of_origin['originOfCountryName']

#Print item
item
