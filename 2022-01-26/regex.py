import requests
import re
import datetime


response=requests.get("https://www.nykaa.com/maybelline-new-york-sensational-liquid-matte-mini-best-babe/p/1495361?ptype=product&skuId=1495361&ef_id=EAIaIQobChMI2ZHE1brK9QIVjplmAh0NxANQEAQYASABEgIUa_D_BwE:G:s&s_kwcid=ALpip%20install%20tkintersudo%20apt%20install%20snapdscrapy%20shellscrapy%20shellxscrapy%20shell&utm_source=GooglePaid&utm_medium=PLA&utm_campaign=PerformanceMaxMakeupcle")
product_name=str(re.findall('"name":"[a-z A-Z].*?",',response.text)[0])
product_name=product_name.split('"')[-2]


ratings=''.join(re.findall('[0-9]<!-- -->/5',response.text))
char=[]
char=[char for char in ratings]
ratings=float(char[0])/float(char[-1])

no_of_ratings=''.join(re.findall('[0-9]*<!-- --> Ratings ',response.text))
no_of_ratings=float(no_of_ratings.split('<')[0])

no_of_reviews=''.join(re.findall('[0-9]*<!-- --> Reviews',response.text))
no_of_reviews=float(no_of_reviews.split('<')[0])

mrp=str(re.findall('"mrp":.[0-9]?,',response.text)[0].split(':')[-1])
mrp=float(mrp.split(',')[0])


expiry_date=''.join(re.findall('"expiry":.*?",',response.text))
expiry_date=expiry_date.split('"')
expiry_date=datetime.datetime.strptime(expiry_date[-2], '%d %B %Y').strftime('%Y/%m/%d')


country_of_origin=''.join(re.findall('"originOfCountryName":.*?",',response.text))
country_of_origin=country_of_origin.split('"')[-2]

item={}
item["product_name"]=product_name
item["ratings"]=ratings
item["no_of_rating"]=no_of_ratings
item["no_of_review"]=no_of_reviews
item["mrp"]=mrp
item["expiry_date"]=expiry_date
item["country_of_origin"]=country_of_origin
print(item)