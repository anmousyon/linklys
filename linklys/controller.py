'''controller class'''

import pprint
from .database import Database
from .newsapi import NewsApi
from .models import Article


class Controller:
    '''controller for entire program'''
    def __init__(self):
        self.database = Database()

    def display_db(self):
        '''
        ***not meant to stay***
        display everything in database
        '''
        for article in Article.select():
            pprint.pprint(article.title)

    def build(self):
        '''build the database'''

        # get all the regular news
        newsapi = NewsApi()
        for source in newsapi.get_sources():
            for article in newsapi.get_articles(source):
                article.save()
