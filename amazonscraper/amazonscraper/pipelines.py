# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class AmazonscraperPipeline:

    def __init__(self):
        self.con = sqlite3.connect('amazon.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.con.execute("""CREATE TABLE IF NOT EXISTS products
                                (name text, price real, discPrice real, link text primary key)""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES (?,?,?,?)""",
                                (item['name'], item['price'], item['discprice'], item['link']))
        self.con.commit()
        return item
