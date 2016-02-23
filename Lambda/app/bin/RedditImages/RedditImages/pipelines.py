# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from scrapy import log
import sqlite3

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RedditImagesPipeline(object):

    def process_item(self, item, spider):
        if item['image']:
            log.msg("Item added successfully.")
            return item
        else:
            del item
            raise DropItem("Non-image thumbnail found: ")


class StoreImage(object):

    def __init__(self):
        self.db = sqlite3.connect('images')
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute('''
                CREATE TABLE IMAGES(IMAGE BLOB, TITLE TEXT, URL TEXT)
            ''')
            self.db.commit()
        except sqlite3.OperationalError:
            self.cursor.execute('''
                DELETE FROM IMAGES
            ''')
            self.db.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        image = item['image'][0]
        url = item['url'][0]
        self.cursor.execute('''
            INSERT INTO IMAGES VALUES (?, ?, ?)
        ''', (image, title, url))
        self.db.commit()
