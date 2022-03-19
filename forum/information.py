# coding:utf-8
from flask import Blueprint, render_template, request, session
from  mapping import  User,Attention
information = Blueprint('information', __name__)
from forum import db, global_config
from  mapping import Article
import json

@information.route('/')
def index():

    id = request.args.get("id")
    uid = session.get("id")
    if not id and not uid:
        return render_template('login.html')

    if not id:
        id = uid

    user = User.query.filter(User.id == f'{id}').one()

    attentionList = db.session.query(User.id, User.username).join(Attention, User.id == Attention.be_attention_user_id).filter(
        Attention.attention_user_id == id).all()

    articleList = Article.query.filter(Article.userid==id).order_by(
        Article.create_time.desc()).slice(0, 5)


    count = db.session.query(User.id, User.username).join(Attention, User.id == Attention.be_attention_user_id).filter(
        Attention.attention_user_id == uid).filter(
        Attention.be_attention_user_id == id).count()

    #status 1 已关注 2 未关注 3未登录 4自己
    if not uid:
        status=3
    elif str(id)!=str(uid) and count>0:
        status=1
    elif str(id)!=str(uid) and count<=0:
        status = 2
    else:
        status = 4

    return render_template('/information.html',user=user,WEBREF=global_config.WEBREF,attentionList=attentionList,articleList=articleList,status=status)


@information.route('/add')
def add():
    return 'admin_add'


@information.route('/show')
def show():
    return 'admin_show'

@information.route('/addAttention',methods=['GET','POST'])
def addAttention():
    data = request.get_data()
    data = json.loads(data)
    id=data['id']
    uid = session.get('id')

    article = Attention(attention_user_id=f'{int(uid)}',be_attention_user_id=f'{int(id)}')
    db.session.add(article)
    db.session.commit()
    return json.dumps({'status': '0', 'errmsg': '登录成功！'}, WEBREF=global_config.WEBREF,ensure_ascii=False)
