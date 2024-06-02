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

    if not re.match(r'^[a-zA-Z0-9]+$', author):
        return "Author nickname should contain only letters and numbers."

    if not re.match(r'^[a-zA-Z\s]+$', title):
        return "Title should contain only letters and spaces."

    if not re.match(r'^[a-zA-Z0-9\s\.,:;!?]+$', description):
        return "Description should contain only letters, numbers, spaces, and punctuation."

    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
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
        json.dump(articles, f)

    articles.sort(key=lambda x: x['date'], reverse=True)
    return bottle.template('articles_template.tpl', articles=articles, year=datetime.now().year)

