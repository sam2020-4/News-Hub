import os

class Config:

    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    CATG_API_BASE_URL = 'https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRECT_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

Config_options = {
    'development':DevConfig,
    'production':ProdConfig
}