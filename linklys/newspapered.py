'''newspaper for articles from other sites'''

import newspaper
from .models import NewspaperArticle
from .analyzer import Analyzer


class Newspapered:
    '''Newspapered class'''
    def __init__(self):
        self.analyzer = Analyzer()

    def load_urls(self):
        '''load urls for sites from file'''
        with open('linklys/sites.txt') as file:
            urls = file.readlines()
        cleaned = [url.strip() for url in urls]
        return cleaned

    def get_site(self, url):
        '''build site using newspaper'''
        site = newspaper.build(url)
        return site

    def get_articles(self, site):
        '''get all articles from site'''
        articles = site.articles
        cleaned = []
        for article in articles:
            to_get = article
            to_get.download()
            to_get.parse()
            if to_get.summary:
                sentiment = self.analyzer.sentiment(to_get.summary)
            else:
                sentiment = "0"
            cleaned.append(
                NewspaperArticle(
                    to_get,
                    sentiment
                )
            )
        return cleaned
