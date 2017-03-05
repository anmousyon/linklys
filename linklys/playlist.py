'''playlist of articles'''

from .database import Database
from .cleaner import Cleaner


class Playlist:
    '''playlist class'''
    def __init__(self):
        self.database = Database()
        self.cleaner = Cleaner()

    def find_article(self, to_add):
        '''find article in database'''
        for article in self.database.articles.find():
            loaded = self.cleaner.load(article)
            if to_add == loaded.data['title']:
                return article

    def add_article(self, to_add):
        '''add article to playlist database'''
        # get all articles already in database
        articles = []
        for article in self.database.playlist.find():
            loaded = self.cleaner.load(article)
            articles.append(loaded.data['title'])

        if not to_add['title'] in articles:
            self.database.playlist.insert_one(to_add)

    def rem_article(self, article):
        '''remove article from playlist database'''
        self.database.playlist.delete_one({'title': article['title']})
