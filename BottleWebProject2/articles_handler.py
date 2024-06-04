import bottle
from bottle import request, redirect, template
import json
import re
from datetime import datetime

# ��������� post-�������
@bottle.route('/submit_article', method='POST')
# ������� ���������� ����� ������
def submit_article():
    author = request.forms.get('author')  # ��������� �������� ������
    title = request.forms.get('title')  # ��������� ��������� ������
    description = request.forms.get('description')  # ��������� �������� ������
    date = request.forms.get('date')  # ��������� ���� ����������
    link = request.forms.get('link')  # ��������� ������

    # �������� �� ������������� �����
    if not (author and title and description and date and link):
        return template('error.tpl', error_message= "All fields are required.", title='Error', year=datetime.now().year)

    # �������� �� ������������ �������� �������
    if not check_author(author):
        return template('error.tpl', error_message="Author nickname should contain only letters and numbers.", title='Error', year=datetime.now().year)

    # �������� �� ������������ ��������� �������
    if not re.match(r'^[a-zA-Z0-9\s\.,-:;\'\"!?]+$', title):
        return template('error.tpl', error_message="Title should contain only letters, numbers, punctuation and spaces.", title='Error', year=datetime.now().year)

    # �������� �� ������������ �������� �������
    if not re.match(r'^[a-zA-Z0-9\s\.,-:;\'\"!?]+$', description):
        return template('error.tpl', error_message="Description should contain only letters, numbers, spaces, and punctuation.", title='Error', year=datetime.now().year)

    # �������� �� ������������ ���� �������
    if not check_date(date):
        return template('error.tpl', error_message="Uncorrect date.", title='Error', year=datetime.now().year)

    articles = []  # ������ ������ ������
    try:
        # ������ ������ �� ����� � ������
        with open('articles.json', 'r') as f:
            articles = json.load(f)
    except FileNotFoundError:
        pass

    # �������� ������� ����� ������
    new_article = {
        'author': author,
        'title': title,
        'description': description,
        'date': date,
        'link': link
    }
    
    # ���������� ������ � ������ ������
    articles.insert(0, new_article)
    
    # ������ ������ � json-����
    with open('articles.json', 'w') as f:
        json.dump(articles, f, indent=4)

    # ���������� ������
    articles.sort(key=lambda x: x['date'], reverse=True)
    
    # ������������ �������� �� �������
    return bottle.template('articles_template.tpl', articles=articles, year=datetime.now().year)

# ������� �������� ����
def check_date(date):
    try:
        # �������� �� ������������ �������
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            # �������� �� ��, ��� ���� �� ������ �������
            if datetime.strptime(date, '%Y-%m-%d') <= datetime.now():
                return True
        return False
    except:
        return False

    # ������� �������� �������� ������
def check_author(author):
    if re.match(r'^[a-zA-Z0-9_]+$', author):
        return True
    return False