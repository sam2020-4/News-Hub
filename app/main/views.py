from flask import render_template,url_for,request,redirect
from .import main
from ..requests import get_source, article_source, get_category,get_headlines

@main.route('/')
def index():
    '''
    method which returns the index page
    '''
    # geting news categories
    source= get_source()
    headlines = get_headlines()

    return render_template('index.html', sources=source, headlines = headlines)

@main.route('/article/<id>')
def article(id):
    '''
    method that return articles data
    '''
    articles = article_source(id)

    return render_template('article.html', articles = articles, id=id)

@main.route('/categories/<catg_name>')
def category(catg_name):
    '''
    method that returns the categories page
    '''
    category = get_category(catg_name)
    title = f'{catg_name}'
    catg = catg_name
    
    return render_template('categories.html', title = title, category = category, catg=catg_name)
