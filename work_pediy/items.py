# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkPediyItem(scrapy.Item):
    # define the fields for your item here like:


    post_title = scrapy.Field()
    post_author = scrapy.Field()
    post_url = scrapy.Field()
    post_content = scrapy.Field()
    post_view = scrapy.Field()
    lastest_time = scrapy.Field()
    '''
    item['post_title'] = post_title
    item['post_author'] = post_author
    item['post_content'] = post_content
    item['post_view'] = post_view
    item['lastest_time'] = lastest_time
    '''
    # name = scrapy.Field()
    pass
