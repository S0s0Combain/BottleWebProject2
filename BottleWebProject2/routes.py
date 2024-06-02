"""
Routes and views for the bottle application.
"""

import bottle
from re import template
from bottle import route, view
from datetime import datetime
from bottle import static_file, template as templ
import articles_handler
import json

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/about_us')
@view('about_us')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/catalog')
@view('catalog')
def about():
    """Renders the catalog page."""
    return dict(
        title='Catalog',
        message='Catalog',
        year=datetime.now().year
    )

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@bottle.route('/articles')
def articles():
    try:
        with open('articles.json', 'r') as f:
            articles = json.load(f)
    except FileNotFoundError:
        articles = []
        with open('articles.json', 'w') as f:
            json.dump(articles, f)

    articles.sort(key=lambda x: x['date'], reverse=True)
    return bottle.template('articles_template.tpl', articles=articles, year=datetime.now().year)


