'''cleaner class'''

import praw
from .models import Article, Post, NewspaperArticle, ArticleSchema
from .analyzer import Analyzer


class Cleaner:
    '''cleans items and dumps/loads them with marshmallow'''
    def __init__(self):
        self.article_schema = ArticleSchema()
        self.analyzer = Analyzer()

    def clean(self, item):
        '''clean a dirty object then dump it'''
        cleaned = self.dump(item)
        return cleaned

    def dump(self, item):
        '''dump a clean object into dict'''
        dumped = self.article_schema.dump(item)
        return dumped

    def load(self, item):
        '''load clean object from dict'''
        if isinstance(item, dict):
            loaded = self.article_schema.load(item)
        else:
            raise TypeError(
                "load only takes dict objects"
            )
        return loaded
