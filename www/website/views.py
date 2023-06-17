from flask import Blueprint, render_template, request, flash, make_response
from flask import Flask, redirect, session

views = Blueprint('views', __name__, template_folder='templates', static_folder='static')


@views.route('/', methods=['GET', 'POST'])
@views.route('/index.html', methods=['GET', 'POST'])
def index_home():
    return render_template('index.html')
