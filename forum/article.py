# coding:utf-8
from flask import Blueprint, render_template, request

article = Blueprint('acticle', __name__)


@article.route('/index')
def index():
    return render_template('admin/index.html')


@article.route('/add')
def add():
    return 'admin_add'


@article.route('/show')
def show():
    return 'admin_show'