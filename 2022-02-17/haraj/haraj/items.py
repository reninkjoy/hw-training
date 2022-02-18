# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HarajItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    broker_display_name = scrapy.Field()
    broker = scrapy.Field()
    category = scrapy.Field()
    category_url = scrapy.Field()
    title = scrapy.Field()
    property_type = scrapy.Field()
    depth = scrapy.Field()
    sub_category_1 = scrapy.Field()
    sub_category_2 = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    price_per = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    furnished = scrapy.Field()
    rera_permit_number = scrapy.Field()
    dtcm_licence = scrapy.Field()
    scraped_ts = scrapy.Field()
    amenities = scrapy.Field()
    details = scrapy.Field()
    agent_name = scrapy.Field()
    number_of_photos = scrapy.Field()
    reference_number = scrapy.Field()
    user_id = scrapy.Field()
    phone_number = scrapy.Field()
    date = scrapy.Field()
    iteration_number = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()

class HarajUrlItem(scrapy.Item):
    url = scrapy.Field()
