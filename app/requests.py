import urllib.request,json
from .models import source, news, category
import request

# getting api key
api_key = None

# getting news
base_url = None
news_url = None
catg_url = None

def configure_request(app):
    global api_key, base_url,news_url,catg_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    news_url = app.config['NEWS_API_BASE_URL']
    catg_url = app.config['CATG_API_BASE_URL']

# Method to get json response
def get_sources(category):
    get_sources_url = base_url.formatt(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_sources = None

        if get_sources_response['sources']:
            news_sources_list = get_sources_response['sources']
            news_sources = process_sources(news_sources_list)

            return news_sources