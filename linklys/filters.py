'''filters for posts'''

from .models import Link


class Filters:
    '''filters class'''
    def __init__(self):
        self.emotions_to_site = {
            'happy': None,
            'sad': None,
            'funny': ['onion', 'cracked', 'clickhole'],
            'serious': ['bbc-news', 'economist', 'guardian', 'time', 'associated'],
            'old_man': ['weather', 'business', 'economist'],
            'flashback': ['wikipedia'],
            'chill': ['buzzfeed', 'youtube', 'polygon'],
            'interesting': ['hacker', 'geographic', 'livescience']
        }
        self.category_to_site = {
            'news': ["google-news", "sky-news", "hindu", "the-huffington-post"],
            'technology': ["techinica", "hacker", "engadget", "techradar"],
            'sports': ["espn", "fox-sports", "football-italia", "espn-cric-info"],
            'business': ["financial", "street", "economist", "business-insider"],
            'enterntainment': ["entertainment", "ign"],
            'gaming': ["ign", "polygon"],
            'music': ["mtv-news", "youtube"],
            'science_and_nature': ["national-geographic", "new-scientist"],
            'trending': None
        }

    def sentiment_filter(self, articles, sort):
        if sort == 'happy':
            filtered = [article for article in articles if article['sentiment'] == '1']
        elif sort == 'sad':
            filtered = [article for article in articles if article['sentiment'] == '0']
        return filtered

    def site_filter(self, articles, sites):
        filtered = []
        for site in sites:
            for article in articles:
                if site in article['source']:
                    filtered.append(article)
        return filtered

    def trending(self, articles):
        return articles

    def filter_articles(self, articles, sort):
        if sort in ['happy', 'sad']:
            filtered = self.sentiment_filter(articles, sort)
        elif sort in self.emotions_to_site.keys():
            filtered = self.site_filter(articles, self.emotions_to_site[sort])
        elif sort == 'trending':
            filtered = self.trending(articles)
        elif sort in self.category_to_site.keys():
            filtered = self.site_filter(articles, self.category_to_site[sort])
        else:
            filtered = articles
        cleaned = []
        for article in filtered:
            cleaned.append(
                Link(
                    url=article['url'],
                    image_url=article['image_url'],
                    title=article['title'],
                    description=article['description'],
                    author=article['author'],
                    created=article['created'],
                    source=article['source']
                )
            )
        return cleaned
