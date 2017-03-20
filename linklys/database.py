'''database class'''

from peewee import SqliteDatabase
from .models import Article, Playlist, PlaylistArticles


class Database:
    '''manages the database'''
    def __init__(self):
        self.database = SqliteDatabase('linklys.db')
        self.load()

    def load(self):
        '''load tables from database'''
        self.database.connect()
        self.database.create_tables(
            [
                Article,
                Playlist,
                PlaylistArticles
            ],
            safe=True
        )
