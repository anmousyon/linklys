'''
linklys - link aggregator designed in the vein of spotify
'''

import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from .builder import build

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
