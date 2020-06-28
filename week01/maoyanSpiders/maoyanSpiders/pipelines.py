# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class MaoyanspidersPipeline:
    def __init__(self):
        columns = ['item_type','name','time']
        file_name = 'maoyan2.csv'
       
        file = open(file_name, 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(file, columns)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item