import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    CATG_API_URL = 'https://newsapi.org/v2/top-headlines?country=de&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRECT_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}