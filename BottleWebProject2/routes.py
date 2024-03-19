"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
from bottle import static_file

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
        year=datetime.now().year,
    )

@route('/catalog')
@view('catalog')
def about():
    """Renders the catalog page."""
    return dict(
        title='Catalog',
        message='Catalog',
        year=datetime.now().year,
        
    )

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')