# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class MaoyanspidersPipeline:
    

    def process_item(self, item, spider):
        name=item['name']
        itemType=item['item_type']
        time=item['time']
        output = f'|{name}|\t|{itemType}|\t|{time}|\n\n'
        with open('maoyan3.csv',mode='a',newline='',encoding='utf-8') as writer:
             writer.write(output)     
        return item