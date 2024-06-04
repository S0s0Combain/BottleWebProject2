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


@route('/reviews')
@view('reviews')  # Это предполагает, что у вас есть шаблон reviews.tpl
def reviews():
    """Renders the reviews page."""
    # Загрузить отзывы из файла или создать новый файл, если его нет
    if not os.path.isfile('reviews.json') or os.path.getsize('reviews.json') == 0:
        reviews = {}
        with open('reviews.json', 'w') as f:
            json.dump(reviews, f)
    else:
        with open('reviews.json', 'r') as f:
            reviews = json.load(f)

    # Сортировать отзывы по дате, начиная с самого нового
    sorted_reviews = sorted(reviews.values(), key=lambda x: x['date'], reverse=True)

    # Возвращаем данные для отображения в шаблоне
    return dict(
        title='Reviews',
        message='Reviews',
        year=datetime.now().year,
        reviews=sorted_reviews
    )


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@bottle.route('/articles')
def articles():
    # ���������, ��� ���� ���������� � �� ����
    if not os.path.isfile('articles.json') or os.path.getsize('articles.json') == 0:
        # ������� ���� � ������ �������
        articles = []
        with open('articles.json', 'w') as f:
            json.dump(articles, f)
    else:
        # ��������� ���������� �����
        with open('articles.json', 'r') as f:
            articles = json.load(f)

    # ��������� ������ �� ����
    articles.sort(key=lambda x: x['date'], reverse=True)

    # ���������� ������ � �������
    return bottle.template('articles_template.tpl', articles=articles, year=datetime.now().year)



