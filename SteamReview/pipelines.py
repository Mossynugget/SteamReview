# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class SteamreviewPipeline(object):
#     def process_item(self, item, spider):
#         return item


from sqlalchemy.orm import sessionmaker
from .models import Reviews, db_connect, create_reviews_table


class LivingSocialPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_reviews_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save reviews in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        review = Reviews(**item)

        try:
            session.add(review)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item