from flask import render_template
from ..requests import get_news
from . import main


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_news = get_news('business')
	technology_news = get_news('technology')
	entertainment_news = get_news('entertainment')
    title = 'Home - Welcome To Prime News'
    message = 'Welcome To Prime News'
    return render_template('index.html' ,message = message, title = title, news = news, sports_news = sports_news, technology_news = technology_news, entertainment_news = entertainment_news) 

@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = movie)    