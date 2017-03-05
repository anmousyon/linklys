'''get all articles needed'''

import requests
from .models import Article, Source
from .analyzer import Analyzer


class NewsApi:
    '''api for all news sources'''
    def __init__(self):
        self.api_key = "678e8e21125d49c9a081c49856ca0bb8"
        self.analyzer = Analyzer()

    def get_sites(self):
        '''load sites from file'''
        with open('linklys/sites.txt') as file:
            sites = file.readlines()
        cleaned = [site.strip() for site in sites]
        return cleaned[:5]

    def get_sources(self):
        '''get sources, using api'''
        resp = requests.get(
            "https://newsapi.org/v1/sources?language=en"
        )
        sources = []
        resp = resp.json()
        for source in resp['sources']:
            if 'latest' in source['sortBysAvailable']:
                sources.append(
                    Source(source)
                )
        return sources

    def get_articles(self, source):
        '''get new articles from source, using api'''
        resp = requests.get(
            "https://newsapi.org/v1/articles?source=" +
            source.label +
            "&sortBy=latest&apiKey=" +
            self.api_key
        )
        articles = []
        resp = resp.json()
        for article in resp['articles']:
            if article['description']:
                sentiment = self.analyzer.sentiment(article['description'])
            else:
                sentiment = "0"
            articles.append(
                Article(
                    article,
                    source,
                    sentiment
                )
            )
        return articles
