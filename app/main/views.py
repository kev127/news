from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

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
        return render_template('index.html' ,message = message, title = title, sources = sources, sports_sources = sports_sources, technology_sources = technology_sources, entertainment_sources = entertainment_sources) 

@main.route('/sources/<int:id>')
def articles(id):

    '''
    View article page function that returns the article details page and its data
    '''
    sources = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title,article = article)    