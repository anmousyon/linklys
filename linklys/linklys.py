'''
linklys - link aggregator designed in the vein of spotify
'''

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from random import shuffle
from .builder import build
from .cleaner import Cleaner
from .database import Database
from .filters import Filters
from .radio import Radio
from .models import Link
from .playlist import Playlist

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('LINKLYS_SETTINGS', silent=True)


@app.cli.command('initdb')
def initdb():
    '''build the database'''
    print('building')
    build()
    print('built')


@app.route('/')
def hello():
    '''say hello'''
    return render_template('homepage.html')


@app.route('/moods')
def show_moods():
    '''show all moods'''
    moods = []
    return render_template('moods.html', moods=moods)


@app.route('/categories')
def show_categories():
    '''show all categories'''
    categories = []
    return render_template('categories.html', categories=categories)


@app.route('/show_posts/<sort>')
def show_posts(sort):
    '''show all posts'''
    database = Database()
    cleaner = Cleaner()
    filters = Filters()
    articles = []
    for article in database.articles.find():
        articles.append((cleaner.load(article)).data)
    to_show = filters.filter_articles(articles, sort)
    shuffle(to_show)
    return render_template('show_posts.html', articles=to_show)


@app.route('/related/<article>')
def related(article):
    '''show related articles'''
    radio = Radio()
    articles = radio.related(article)
    cleaned = []
    for article in articles:
        dup = False
        for clean in cleaned:
            if article['url'] in clean.url:
                dup = True
        if not dup:
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
    cleaned = list(set(cleaned))
    shuffle(cleaned)
    return render_template('show_posts.html', articles=cleaned)


@app.route('/playlist/<title>')
def add_post(title):
    '''add post to playlist'''
    playlist = Playlist()
    database = Database()
    cleaner = Cleaner()
    to_add = playlist.find_article(title)
    playlist.add_article(to_add)
    articles = []
    for article in database.playlist.find():
        articles.append((cleaner.load(article)).data)
    cleaned = []
    for article in articles:
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
    return render_template('playlist.html', articles=cleaned)


@app.route('/playlist/<title>')
def rem_post(title):
    '''add post to playlist'''
    playlist = Playlist()
    database = Database()
    cleaner = Cleaner()
    to_rem = playlist.find_article(title)
    playlist.rem_article(to_rem)
    articles = []
    for article in database.playlist.find():
        articles.append((cleaner.load(article)).data)
    cleaned = []
    for article in articles:
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
    return render_template('playlist.html', articles=cleaned)


@app.route('/playlist')
def show_playlist():
    '''show playlist'''
    database = Database()
    cleaner = Cleaner()
    articles = []
    for article in database.playlist.find():
        articles.append((cleaner.load(article)).data)
    cleaned = []
    for article in articles:
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
    return render_template('playlist.html', articles=cleaned)
