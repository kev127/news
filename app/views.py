from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_news = get_news('business')
	technology_news = get_news('technology')
	entertainment_news = get_news('entertainment')
    title = 'Home - Welcome To Prime News'
    message = 'Welcome To Prime News'
    return render_template('index.html' ,message = message, title = title, news = news, sports_news = sports_news, technology_news = technology_news, entertainment_news = entertainment_news) )