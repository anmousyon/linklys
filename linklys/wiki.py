'''wikipedia articles for flashback'''

import wikipedia
from .models import WikipediaArticle
from .analyzer import Analyzer


class Wiki:
    '''Wiki class'''
    def __init__(self):
        self.analyzer = Analyzer()

    def load_topics(self):
        '''load wiki topics from file'''
        with open('linklys/topics.txt') as file:
            topics = file.readlines()
        cleaned = [topic.strip() for topic in topics]
        return cleaned

    def get_articles(self):
        topics = self.load_topics()
        cleaned = []
        for topic in topics:
            article = wikipedia.page(topic)
            summary = article.summary
            if summary:
                sentiment = self.analyzer.sentiment(summary)
            else:
                sentiment = "0"
            cleaned.append(
                WikipediaArticle(
                    article,
                    sentiment
                )
            )
        return cleaned
