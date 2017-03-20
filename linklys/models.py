'''post and comment schemas'''

from peewee import SqliteDatabase, Model, TextField

DATABASE = SqliteDatabase('linklys.db')


class Article(Model):
    '''article schema for database'''
    url = TextField()
    image_url = TextField()
    title = TextField()
    description = TextField()
    author = TextField()
    created = TextField()
    sentiment = TextField()
    category = TextField()
    source = TextField()

    class Meta:
        database = DATABASE


class Playlist(Model):
    '''playlist schema for database'''

    class Meta:
        database = DATABASE


class PlaylistArticles(Model):
    '''playilstarticles schema for database'''

    class Meta:
        database = DATABASE


class Source:
    '''source class'''
    def __init__(self, label, name, description, url, category, language):
        self.label = label
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language


class Display_Article:
    '''display article class'''


class ML_Article: 
    '''ml article class'''