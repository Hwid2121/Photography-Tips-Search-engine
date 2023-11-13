# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy import settings
from scrapy.exceptions import DropItem
import logging
from scrapy.utils.project import get_project_settings
from .items import PhotographyTipsScraperItem

logger = logging.getLogger()


class ContentPipeline:

    def process_item(self, item, spider):
        pass


settings = get_project_settings()


class MongoDBPipeline:

    def __init__(self):
        conn = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db = conn[settings.get('MONGODB_DB')]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):

        # clean the db
        adapter = ItemAdapter(item)
        if adapter.get('title') is not None:
            title = adapter['title']
            title = ''.join(title).replace('\r\n', '').strip().rstrip()
            adapter['title'] = title
        if adapter.get('content') is not None:
            content = adapter['content']
            content = ''.join(content).replace('\r\n', '').strip().rstrip()
            adapter['content'] = content
        if adapter.get('title') is None:
            raise DropItem("Missing title in %s" % item)
        elif adapter.get('content') is None:
            raise DropItem("Missing content in %s" % item)
        elif adapter.get('url') is None:
            raise DropItem("Missing url in %s" % item)
        else:
            self.collection.update_one(dict(item), {'$set': dict(item)}, upsert=True)
            logger.debug("Post added to MongoDB")

        return item
