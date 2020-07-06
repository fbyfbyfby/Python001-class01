# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import csv
from .SQLCONFIG import ConnDB,dbInfo,sqls

DIC_INFO = {'名称': [], '类型': [], '上映时间': []} 
db_mysql = ConnDB(dbInfo, sqls)


class MaoyanspidersPipeline:  
    def process_item(self, item, spider):
        DIC_INFO['名称'] = [item['name']]
        DIC_INFO['类型'] = [item['item_type']]
        DIC_INFO['上映时间'] = [item['time']]

        tuple_to_insert = (item['name'], item['item_type'], item['time'])
        db_mysql.run(tuple_to_insert)

        return item