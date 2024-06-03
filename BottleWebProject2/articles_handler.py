import bottle
from bottle import request, redirect, template
import json
import re
from datetime import datetime

@bottle.route('/submit_article', method='POST')
def submit_article():
    author = request.forms.get('author')
    title = request.forms.get('title')
    description = request.forms.get('description')
    date = request.forms.get('date')
    link = request.forms.get('link')

    if not (author and title and description and date and link):
        return "All fields are required."

    if not check_author(author):
        return "Author nickname should contain only letters and numbers."

    if not re.match(r'^[a-zA-Z0-9\s\.,-:;\'\"!?]+$', title):
        return "Title should contain only letters and spaces."

    if not re.match(r'^[a-zA-Z0-9\s\.,-:;\'\"!?]+$', description):
        return "Description should contain only letters, numbers, spaces, and punctuation."

    if not check_date(date):
        return "Date should be in YYYY-MM-DD format."


    articles = []
    try:
        with open('articles.json', 'r') as f:
            articles = json.load(f)
    except FileNotFoundError:
        pass

    new_article = {
        'author': author,
        'title': title,
        'description': description,
        'date': date,
        'link': link
    }
    articles.append(new_article)

    with open('articles.json', 'w') as f:
        json.dump(articles, f, indent=4)

    articles.sort(key=lambda x: x['date'], reverse=True)
    return bottle.template('articles_template.tpl', articles=articles, year=datetime.now().year)

def check_date(date):
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        return True
    return False

def check_author(author):
    if re.match(r'^[a-zA-Z0-9_]+$', author):
        return True
    return False