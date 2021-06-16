# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import pymongo
import csv

class WorkPediyPipeline(object):
    def __init__(self,ip=''):
        # 创建一个mongo数据库连接
        self.client = pymongo.MongoClient()
        # 链接至一个数据库
        self.db = self.client['bbs']
        # # 设置代理ip
        # self.ip = ip
        pass
    def process_item(self, item, spider):
        # 添加代理ip
        # thisip = random.choice(IPPOOL)
        # request.meta["proxy"] = "http://" + thisip["ipaddr"]
        # 保存数据
        self.db['pcdiy'].update({'post_url':item['post_url']},{'$set':dict(item)},True)
        # print(item)
        # 保存到csv
        f = open(file='pcdiy.csv',mode='a+',encoding='utf-8-sig')
        write = csv.writer(f)
        write.writerows((item['post_title'],item['post_author'],
                         item['post_url'],item['post_content'],
                         item['post_view'],item['lastest_time']))
        return item
