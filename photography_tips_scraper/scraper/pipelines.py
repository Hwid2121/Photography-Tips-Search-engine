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
import re

logger = logging.getLogger()
settings = get_project_settings()


class ContentPipeline:

    def process_item(self, item, spider):
        pass


class MongoDBPipeline:

    def __init__(self):
        conn = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db = conn[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]

    def process_item(self, item, spider):
        # Clean the db
        adapter = ItemAdapter(item)

        # Clean title
        if adapter.get('title') is not None:
            title = ''.join(adapter['title']).replace('\r\n', '').strip()
            adapter['title'] = title
        else:
            raise DropItem("Missing title in %s" % item)

        # Clean content
        if adapter.get('content') is not None:
            content = (''.join(adapter['content']).replace('\r\n', '')
                       .replace('\n', '').replace('\t', '')
                       .replace('\r', '').replace('\xa0', '').
                       strip())

            # Add your content cleaning regex here
            content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content, flags=re.DOTALL)
            content = re.sub(r'!function\s*\([^)]*\)\s*{[^}]*}', '', content)
            content = re.sub(r'^\d+\s*', '', content)
            content = re.sub(r'^\s*\d+\s*$', '', content, flags=re.MULTILINE)


            adapter['content'] = content
        else:
            raise DropItem("Missing content in %s" % item)
        # Check for other required fields
        if adapter.get('url') is None:
            raise DropItem("Missing URL in %s" % item)

        # Update MongoDB collection
        self.collection.update_one(dict(item), {'$set': dict(item)}, upsert=True)
        logger.debug("Post added to MongoDB")

        return item
