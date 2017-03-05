'''find related articles in database'''

import RAKE
from .database import Database
from .cleaner import Cleaner


class Radio:
    '''radio for related articles'''
    def __init__(self):
        self.database = Database()
        self.cleaner = Cleaner()
        self.filter = RAKE.Rake('stoplist.txt')

    def get_keywords(self, article):
        '''find keywords of article'''
        if article:
            keywords = self.filter.run(article)
            actual = []
            for keyword in keywords:
                actual.append(keyword[0])
            return actual
        else:
            return ''

    def search_db(self, keywords):
        '''search database for keywords'''
        full_list = []
        for article in self.database.articles.find():
            cleaned = (self.cleaner.load(article)).data
            for keyword in keywords:
                if str(keyword) in cleaned['title']:
                    full_list.append(cleaned)
        return full_list

    def related(self, article):
        '''find articles related to current article'''
        print('article: ' + article)
        keywords = self.get_keywords(article)
        articles = self.search_db(keywords)
        return articles
