# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestateItem(scrapy.Item):
    status = scrapy.Field()             # status
    title = scrapy.Field()              # title
    vraagprijs = scrapy.Field()         # price
    bouwjaar = scrapy.Field()           # construction_year
    soort_object = scrapy.Field()       # type of object
    woonoppervlakte = scrapy.Field()    # living area
    inhoud = scrapy.Field()             # content
    aantal_kamers = scrapy.Field()      # num of rooms
    aantal_slaapkamers = scrapy.Field() # num of bedrooms
    aantal_badkamers = scrapy.Field()   # num of bathrooms
    aantal_woonlagen = scrapy.Field()   # num of floors