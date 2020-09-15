from flask import render_template
from . import main

def four_Ow_four(error):
    '''
    method to render error 404 page
    '''

    return render_template('fourOwfour.html'),404
