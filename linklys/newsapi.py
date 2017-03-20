'''get all articles needed'''

import requests
from .models import Article, Source
from .analyzer import Analyzer


class NewsApi:
    '''api for all news sources'''
    def __init__(self):
        self.api = "678e8e21125d49c9a081c49856ca0bb8"
        self.base = "https://newsapi.org/v1/articles?source="
        self.sort = "&sortBy=latest&apiKey="
        self.analyzer = Analyzer()

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
                    Source(
                        source['id'],
                        source['name'],
                        source['description'],
                        source['url'],
                        source['category'],
                        source['language']
                    )
                )
        return sources

    def get_articles(self, source):
        '''get new articles from source, using api'''
        resp = requests.get(
            '{}{}{}{}'.format(self.base, source.label, self.sort, self.api)
        ).json()
        articles = []
        for article in resp['articles']:
            if article['description']:
                sentiment = self.analyzer.sentiment(article['description'])
                description = article["description"]
            else:
                sentiment = "0"
                description = "none"
            if article["author"]:
                author = article["author"]
            else:
                author = "none"
            if article["urlToImage"]:
                image_url = article["urlToImage"]
            else:
                image_url = "none"
            if article["publishedAt"]:
                created = article["publishedAt"]
            else:
                created = "none"
            if article["url"]:
                url = article["url"]
            else:
                url = "none"
            if article["title"]:
                title = article["title"]
            else:
                title = "none"
            articles.append(
                Article(
                    url=url,
                    image_url=image_url,
                    title=title,
                    description=description,
                    author=author,
                    created=created,
                    sentiment=sentiment,
                    category=source.category,
                    source=source.url
                )
            )
        return articles
