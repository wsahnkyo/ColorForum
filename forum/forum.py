# coding:utf-8
from flask import Blueprint, render_template, request
from flask import session
import json
import datetime

forum = Blueprint('forum', __name__)
from  mapping import Article,User,UserArticle,ArticleComment
from forum import db, global_config

@forum.route('/')
def index():
    title =  request.args.get('title')
    page_index = request.args.get('page_index')
    if not page_index or int(page_index)<1:
        page_index=1
    if not title:
        articleList = Article.query.order_by(
            Article.create_time.desc()).slice((int(page_index) - 1) *20, int(page_index) * 20)
    else:
        articleList = Article.query.filter(Article.title.like('%{keyword}%'.format(keyword=title))).order_by(
            Article.create_time.desc()).slice((int(page_index)  - 1) *20, int(page_index)  * 20)
    return render_template('forum.html',articleList=articleList,WEBREF=global_config.WEBREF,title=title,page_index=page_index,sessionid=session.get('id'))


@forum.route('/information')
def information():
    articleid = request.args.get("articleid")
    article = Article.query.filter(Article.articleid == f'{articleid}').one()

    user = User.query.filter(User.id==article.userid).one()
    id =session.get("id")
    articleCommentList =db.session.query(ArticleComment, User).join(User,User.id==ArticleComment.userid).filter(ArticleComment.articleid==articleid).all()
    return render_template('forum_information.html',article=article,user=user,WEBREF=global_config.WEBREF,articleCommentList=articleCommentList,id=id)


@forum.route('/submit')
def submit():
    id=session.get("id")
    if not id:
        return render_template('login.html')
    return render_template('forum_submit.html',WEBREF=global_config.WEBREF)

@forum.route('/add',methods=['GET','POST'])
def add():
    data = request.get_data()
    data = json.loads(data)
    title = data['title']
    content = data['content']
    id = session.get('id')

    article = Article(userid=f'{int(id)}', title=f'{title}', content=f'{content}',create_time=f'{datetime.datetime.now()}')
    db.session.add(article)
    db.session.commit()
    return json.dumps({'status': '0', 'errmsg': '登录成功！'}, ensure_ascii=False)

@forum.route('/addScore',methods=['GET','POST'])
def addScore():
    id = session.get('id')
    data = request.get_data()
    data = json.loads(data)
    articleid = data['articleid']
    score = data['score']
    userArticle = UserArticle.query.filter(UserArticle.articleid==articleid).filter(UserArticle.userid==id).one()
    #如果没有评分记录就添加
    if not userArticle:
        userArticle = UserArticle(userid=f'{int(id)}', articleid=f'{int(articleid)}', score=f'{score}')
        db.session.add(userArticle)
        db.session.commit()
    #如果有就更新
    else:
        UserArticle.query.filter(UserArticle.articleid==articleid).filter(UserArticle.userid==id).update({'score': score})
        db.session.commit()

    return json.dumps({'status': '0', 'errmsg': '登录成功！'}, ensure_ascii=False)

@forum.route('/addComment',methods=['GET','POST'])
def addComment():
    id = session.get('id')
    data = request.get_data()
    data = json.loads(data)
    articleid = data['articleid']
    comment = data['comment']

    articleComment = ArticleComment(userid=f'{int(id)}', articleid=f'{int(articleid)}', comment=f'{comment}')
    db.session.add(articleComment)
    db.session.commit()

    return json.dumps({'status': '0', 'errmsg': '登录成功！'}, ensure_ascii=False)

