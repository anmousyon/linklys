'''post and comment schemas'''

from marshmallow import Schema, fields


class ArticleSchema(Schema):
    '''marshmallow schema for posts'''
    url = fields.Str()
    image_url = fields.Str()
    title = fields.Str()
    description = fields.Str()
    author = fields.Str()
    created = fields.Str()
    sentiment = fields.Str()
    category = fields.Str()
    source = fields.Str()


class Article:
    '''article class'''
    def __init__(self, article, source, sentiment):
        self.url = article['url']
        if article['urlToImage']:
            self.image_url = article['urlToImage']
        else:
            self.image_url = "http://www.jakesonline.org/black.gif"
        if article['title']:
            self.title = article['title']
        else:
            self.title = "Not Available"
        if article['description']:
            self.description = article['description']
        else:
            self.description = "Not Available"
        if article['author']:
            self.author = article['author']
        else:
            self.author = "Not Available"
        if article['publishedAt']:
            self.created = article['publishedAt']
        else:
            self.created = "Not Available"
        self.sentiment = sentiment
        if source.category:
            self.category = source.category
        else:
            self.category = "General"
        if source.url:
            self.source = source.url
        else:
            self.source = "Not Available"


class Source:
    '''source class'''
    def __init__(self, source):
        self.label = source['id']
        self.name = source['name']
        self.description = source['description']
        self.url = source['url']
        self.category = source['category']
        self.language = source['language']


class Post:
    '''post class'''
    def __init__(self, post, sentiment):
        self.url = post.url
        self.image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Reddit.svg/1024px-Reddit.svg.png"
        self.title = post.title
        self.description = "pulled from reddit"
        self.author = str(post.author)
        self.created = str(post.created)
        self.sentiment = sentiment
        self.category = str(post.subreddit)
        self.source = "http://youtube.com"


class NewspaperArticle:
    '''newspaper article class'''
    def __init__(self, article, sentiment):
        self.url = article.url
        if article.top_image:
            self.image_url = article.top_image
        else:
            self.image_url = "http://www.jakesonline.org/black.gif"
        if article.title:
            self.title = article.title
        else:
            self.title = "Not Available"
        if article.summary:
            self.description = article.summary
        else:
            self.description = "Not Available"
        if article.authors:
            if article.authors[0]:
                self.author = article.authors[0]
            else:
                self.author = "Not Available"
        else:
            self.author = "Not Available"
        if article.publish_date:
            self.created = article.publish_date
        else:
            self.created = "Not Available"
        self.sentiment = sentiment
        if article.tags:
            self.category = list(article.tags)[0]
        else:
            self.category = "general"
        if article.source_url:
            self.source = article.source_url
        else:
            self.source = "Not Available"


class WikipediaArticle:
    '''wikipedia article class'''
    def __init__(self, article, sentiment):
        if article.url:
            self.url = article.url
        else:
            self.url = "Not Available"
        self.image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1122px-Wikipedia-logo-v2.svg.png"
        if article.title:
            self.title = article.title
        else:
            self.title = "Not Available"
        if article.summary:
            self.description = article.summary
        else:
            self.description = "Not Available"
        self.author = "community"
        self.created = "continuous"
        self.sentiment = sentiment
        if article.categories[0]:
            self.category = article.categories[0]
        else:
            self.category = "General"
        self.source = "http://wikipedia.com"


class Link:
    '''link class'''
    def __init__(self, url, image_url, title, description, author, created, source):
        self.url = url
        self.image_url = image_url
        self.title = title
        self.description = description
        self.author = author
        self.created = created
        self.source = source
