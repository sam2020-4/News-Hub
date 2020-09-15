from flask import render_template
from.import main
from ..requests import get_sources, get_news, get_category

@main.route('/')
def index():
    # page which returns the index page

    # geting news categories
    general_news = get_sources('general')
    other_news = get_sources('otherNews')

    title = 'News-Hub'
    return render_template('index.html', title = title, general= general_news, otherNews = other_news)

@main.route('/news/<id>')
def news(id):
    # method that return news data
    news_articles = get_news(id)

    return render_template('news.html', news=news_articles)

@main.route('/categories/<category>')
def general(category):

    #method that returns the main page

    news_categories_articles = get_category(category)
    return render_template('general.html', general = news_categories_articles)

@main.route('/categories/<category>')
def otheraNews(category):

    #method that returns the other news page

    news_categories_articles = get_category(category)
    return render_template('otherNews.html', otherNews = news_categories_articles)
