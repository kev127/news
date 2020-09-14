from flask import render_template
from .requests import get_sources
from . import main


# Views
@main.route('/')
def index():

        '''
        View root page function that returns the index page and its data
        '''
        sources = get_sources()
        business_sources = get_sources('business')
        technology_sources = get_sources('technology')
        entertainment_sources = get_sources('entertainment')
        title = 'Home - Welcome To Prime News'
        message = 'Welcome To Prime News'
        return render_template('index.html' ,message = message, title = title, sources = sources, sports_news = sports_news, technology_news = technology_news, entertainment_news = entertainment_news) 

@main.route('/sources/<int:id>')
def articles(id):

    '''
    View article page function that returns the article details page and its data
    '''
    sources = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title,article = article)    