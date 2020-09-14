import urllib.request,json
from .models import Sources, Articles


# Getting api key
api_key = None

# Getting the sources base url
base_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']


def get_sources(category):
    '''
        Function that gets the json response to our url request
        '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_sources_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_sources_response['results']
            news_results = process_results(sources_results_list)

    return sources_results


def process_sources(sources_list):
    '''
        Function that processes the sources sources results and turns them into a list of objects

        Args:
         news_list: A list of dictionaries that contain sources sources details

        Returns:
         news_results: A list of sources objects
        '''
    sources_results = []

    for sources_item in sources_list:
        id = sources_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        news_object = sources(id,title,description,url,category,country,language)
        news_results.append(news_object)

    return sources_results 

def get_articles(id):
    '''
        Function that processes the articles and returns a list of articles objects
        '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object


def process_articles(articles_list):
    '''
        '''
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')

        if image:
            articles_result = Articles(
                id, author, title, description, url)
            articles_object.append(articles_result)

        return articles_object       