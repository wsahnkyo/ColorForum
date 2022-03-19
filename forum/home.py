# coding:utf-8
from flask import Blueprint, render_template, request

home = Blueprint('home', __name__)

from forum import db, global_config

@home.route('/')
def index():
    dict = {"1": "黑色系", "2": "蓝色系", "3": "黄色系", "4": "绿色系", "5": "水色系", "6": "红色系", "7": "苍色系", "8": "灰白色系",
            "9": "金银色系","10":"紫色系"}

    return render_template('home.html',WEBREF=global_config.WEBREF,dict=dict)


