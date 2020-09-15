import urllib.request,json
from .models import Article, Source, Category, Headlines

# getting api key
api_key = None

# getting news source url
source_url = None
catg_url = None

def configure_request(app):
    global api_key,source_url,catg_url
    api_key = app.config['NEWS_API_KEY']    
    source_url = app.config['NEWS_API_SOURCE_URL']
    catg_url = app.config['CATG_API_URL']

# Method to get json response
def get_source():
    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)


        source_results = None        

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

            return source_results

# method to define the processes of news source
def process_results(source_list):
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)   

    return source_results

def article_source(id):
    article_source_url ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)

    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['artcles']
            article_source_results = process_articles_results(article_source_list)

    return article_source_results

# method to transforn news sources to objects
def process_articles_results(news):
    
    article_source_results = []

    for article in news:
        
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        if url:
            article_objects = Article(author,title, description, url,urlToImage,publishedAt)
            article_source_results.append(article.objects)

    return article_source_results

#method to get json url request
def get_category(catg_name):
    get_category_url = catg_url.format(catg_name,api_key)
    print(get_category_url)

    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_results = process_articles_results(get_category_list)
          
    return get_category_results

# method that gets the response to the category json
def get_headlines():
    get_headlines_url ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)
          
    return get_headlines_results
