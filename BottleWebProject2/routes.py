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
import os

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
    # Проверяем, что файл существует и не пуст
    if not os.path.isfile('articles.json') or os.path.getsize('articles.json') == 0:
        # Создаем файл с пустым списком
        articles = []
        with open('articles.json', 'w') as f:
            json.dump(articles, f)
    else:
        # Считываем содержимое файла
        with open('articles.json', 'r') as f:
            articles = json.load(f)

    # Сортируем статьи по дате
    articles.sort(key=lambda x: x['date'], reverse=True)

    # Возвращаем шаблон с данными
    return bottle.template('articles_template.tpl', articles=articles, year=datetime.now().year)



