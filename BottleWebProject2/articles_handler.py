import bottle
from bottle import request, redirect, template
import json
import re
from datetime import datetime

# получение post-запроса
@bottle.route('/submit_article', method='POST')
# функция добавления новой статьи
def submit_article():
    author = request.forms.get('author')  # получение никнейма автора
    title = request.forms.get('title')  # получение заголовка статьи
    description = request.forms.get('description')  # получение описания статьи
    date = request.forms.get('date')  # получение даты публикации
    link = request.forms.get('link')  # получение ссылки

    # проверка на заполненность полей
    if not (author and title and description and date and link):
        return template('error.tpl', error_message= "All fields are required.", title='Error', year=datetime.now().year)

    # проверка на соответствие никнейма формату
    if not check_author(author):
        return template('error.tpl', error_message="Author nickname should contain only letters and numbers.", title='Error', year=datetime.now().year)

    # проверка на соответствие заголовка формату
    if not re.match(r'^[a-zA-Z0-9\s\.,-:;\'\"!?]+$', title):
        return template('error.tpl', error_message="Title should contain only letters, numbers, punctuation and spaces.", title='Error', year=datetime.now().year)

    # проверка на соответствие описания формату
    if not re.match(r'^[a-zA-Z0-9\s\.,-:;\'\"!?]+$', description):
        return template('error.tpl', error_message="Description should contain only letters, numbers, spaces, and punctuation.", title='Error', year=datetime.now().year)

    # првоерка на соответствие даты формату
    if not check_date(date):
        return template('error.tpl', error_message="Uncorrect date.", title='Error', year=datetime.now().year)

    articles = []  # пустой список статей
    try:
        # чтение данных из файла в список
        with open('articles.json', 'r') as f:
            articles = json.load(f)
    except FileNotFoundError:
        pass

    # создание словаря новой статьи
    new_article = {
        'author': author,
        'title': title,
        'description': description,
        'date': date,
        'link': link
    }
    
    # добавление статьи в список статей
    articles.insert(0, new_article)
    
    # запись списка в json-файл
    with open('articles.json', 'w') as f:
        json.dump(articles, f, indent=4)

    # сортировка списка
    articles.sort(key=lambda x: x['date'], reverse=True)
    
    # перезагрузка страницы со статьям
    return bottle.template('articles_template.tpl', articles=articles, year=datetime.now().year)

# функция проверки даты
def check_date(date):
    try:
        # проверка на соответствие формату
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            # проверка на то, что дата не больше текущей
            if datetime.strptime(date, '%Y-%m-%d') <= datetime.now():
                return True
        return False
    except:
        return False

    # функция проверки никнейма автора
def check_author(author):
    if re.match(r'^[a-zA-Z0-9_]+$', author):
        return True
    return False