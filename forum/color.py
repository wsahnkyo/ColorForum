# coding:utf-8
from flask import Blueprint, render_template, request
from flask import session
import datetime
from  mapping import Color,Article,UserArticle
from forum import db, global_config,suanfa
import json


color = Blueprint('color', __name__)
@color.route('/')
def index():
    title = request.args.get('title')
    page_index = request.args.get('page_index')
    classify = request.args.get('classify')
    map = []
    if title:
        like = '%{}%'.format(title)
        map.append(Color.title.like(like))

    if classify:
        map.append(Color.classify == classify)

    if not page_index or int(page_index) < 1:
        page_index = 1

    colorList = Color.query.filter(*map).order_by(Color.create_time.desc()).slice((int(page_index) - 1) * 20, int(page_index) * 20)

    return render_template('color.html', colorList=colorList, WEBREF=global_config.WEBREF, title=title,
                           page_index=page_index)


@color.route('/information')
def information():
    colorid = request.args.get("colorid")
    color = Color.query.filter(Color.colorid == f'{colorid}').one()
    dict = {"1": "黑色系", "2": "蓝色系", "3": "黄色系", "4": "绿色系", "5": "水色系", "6": "红色系", "7": "苍色系", "8": "灰白色系",
            "9": "金银色系","10":"紫色系"}
    # color.classify=dict[color.classify]
    id=session.get("id")
    if not id:
        articleList = Article.query.filter(Article.title.like('%{keyword}%'.format(keyword=color.title))).order_by(Article.create_time.desc()).all()
    else:

        userArticleList = UserArticle.query.all()
        bookid_list, nearuser =suanfa.adjustrecommend(str(id),userArticleList)
        articleList = Article.query.filter(Article.articleid.in_(bookid_list)).order_by(
            Article.create_time.desc()).all()

    return render_template('color_information.html',color=color,articleList=articleList, WEBREF=global_config.WEBREF,dict=dict)


@color.route('/submit')
def submit():
    id=session.get("id")
    if not id:
        return render_template('login.html')
    dict = {"1": "黑色系", "2": "蓝色系", "3": "黄色系", "4": "绿色系", "5": "水色系", "6": "红色系", "7": "苍色系", "8": "灰白色系",
            "9": "金银色系","10":"紫色系"}
    return render_template('color_submit.html',WEBREF=global_config.WEBREF,dict=dict)

@color.route('/add',methods=['GET','POST'])
def add():
    data = request.get_data()
    data = json.loads(data)
    title = data['title']
    content = data['content']
    classify = data['classify']
    code = data['code']
    id = session.get('id')

    article = Color(userid=f'{int(id)}', title=f'{title}', content=f'{content}',classify=f'{classify}',code=f'{code}')
    db.session.add(article)
    db.session.commit()
    return json.dumps({'status': '0', 'errmsg': '登录成功！'}, ensure_ascii=False)

