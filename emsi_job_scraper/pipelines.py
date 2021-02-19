# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Imports
from itemadapter import ItemAdapter
import logging
import json
from datetime import datetime

# Normalize the categories and job title
class CategoryOrganizerPipeline:
    def process_item(self, item, spider):
        item["location"] = item["categories"]["location"]
        del item["categories"]["location"]
        item["team"] = item["categories"]["team"]
        del item["categories"]["team"]
        title_attrs = str.split(item["job_title"], ",")

        if "department" in item["categories"]:
            item["department"] = item["categories"]["department"]
            del item["categories"]["department"]
        if "commitment" in item["categories"]:
            item["commitment"] = item["categories"]["commitment"]
            del item["categories"]["commitment"]

        item["other_categories"] = item["categories"]
        del item["categories"]

        item["job_title"] = title_attrs[0]
        item["job_subtitle"] = str.strip(",".join(title_attrs[1:]))
        return item
