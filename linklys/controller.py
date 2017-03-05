'''controller class'''

import pprint
from .database import Database
from .reddit import Reddit
from .cleaner import Cleaner
from .newsapi import NewsApi
from .newspapered import Newspapered
from .wiki import Wiki


class Controller:
    '''controller for entire program'''
    def __init__(self):
        self.database = Database()

    def display_db(self):
        '''
        ***not meant to stay***
        display everything in database
        '''
        cleaner = Cleaner()
        for article in self.database.articles.find():
            loaded = cleaner.load(article)
            pprint.pprint(loaded.data['title'])

    def build(self):
        '''build the database'''
        cleaner = Cleaner()

        # get all articles already in database
        articles = []
        for article in self.database.articles.find():
            loaded = cleaner.load(article)
            articles.append(loaded.data['title'])

        # get all the regular news
        counter = 0
        print('\tnewsapi')
        newsapi = NewsApi()
        for source in newsapi.get_sources():
            for article in newsapi.get_articles(source):
                if article.title not in articles:
                    counter += 1
                    self.database.insert(cleaner.clean(article))
        print("\t\t" + str(counter))

        # get music and videos
        counter = 0
        print('\treddit')
        reddit = Reddit()
        for subreddit in reddit.get_subreddits():
            for post in reddit.get_posts(subreddit):
                # only take links to youtube (music and videos)
                if post.title not in articles and "youtube.com" in post.url:
                    counter += 1
                    self.database.insert(cleaner.clean(post))
        print("\t\t" + str(counter))

        # get articles from unique/unpopular sites not covered by newsapi
        counter = 0
        print('\tnewspaper')
        newspapered = Newspapered()
        for site in newspapered.load_urls():
            site = newspapered.get_site(site)
            for article in newspapered.get_articles(site):
                if article.title not in articles:
                    counter += 1
                    self.database.insert(cleaner.clean(article))
        print("\t\t" + str(counter))

        # get wikipedia articles about interesting topics from yesteryear
        print('\twikipedia')
        counter = 0
        wiki = Wiki()
        topics = wiki.get_articles()
        for article in topics:
            if article.title not in articles:
                counter += 1
                self.database.insert(cleaner.clean(article))
        print("\t\t" + str(counter))
