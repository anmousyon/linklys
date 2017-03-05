'''database class'''

from pymongo import MongoClient
from marshmallow import MarshalResult


class Database:
    '''manages the database'''
    def __init__(self):
        self.client = MongoClient()
        self.articles, self.playlist = self.load()

        # emptying database before each run for now
        # self.clear()

    def clear(self):
        '''clear database tables'''
        self.playlist.delete_many({})

    def load(self):
        '''load tables from database'''
        database = self.client.database
        return database.articles, database.playlist

    def insert(self, item):
        '''insert item into database'''
        if isinstance(item, MarshalResult):
            self.articles.insert_one(item.data)
        else:
            print(item.data)
            raise TypeError(
                "insert only takes MarshalResult objects"
            )
