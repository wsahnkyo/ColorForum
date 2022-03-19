from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
import configs
import time

from sqlalchemy.sql import func

db = SQLAlchemy()  # 通过类`SQLAlchemy`来连接数据库
app = Flask(__name__)
app.config.from_object(configs.Config)
db = SQLAlchemy(app)

def current_timestamp():
    return int(time.time())

class User(db.Model):
    __tablename__ = 'user'  # 如果不指定表名，会默认以这个类名的小写为表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False,)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    telephone = db.Column(db.String(255))
    address = db.Column(db.String(255))


class Article(db.Model):
    __tablename__ = 'article'  # 如果不指定表名，会默认以这个类名的小写为表名
    articleid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer,db.ForeignKey('user.id'))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    href = db.Column(db.Text)
    create_time = db.Column(db.DateTime,server_default=func.now())
    type =db.Column(db.String(1),default='2')

class Color(db.Model):
    __tablename__ = 'color'  # 如果不指定表名，会默认以这个类名的小写为表名
    colorid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer,db.ForeignKey('user.id'))
    title = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime,server_default=func.now())
    classify =db.Column(db.String(1),default='1')

class Attention(db.Model):
    __tablename__ = 'attention'  # 如果不指定表名，会默认以这个类名的小写为表名
    attentionid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    attention_user_id = db.Column(db.Integer)
    be_attention_user_id = db.Column(db.String(255))

class UserArticle(db.Model):
    __tablename__ = 'user_article'  # 如果不指定表名，会默认以这个类名的小写为表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer)
    articleid = db.Column(db.Integer)
    score=db.Column(db.Float)

class ArticleComment(db.Model):
    __tablename__ = 'article_comment'  # 如果不指定表名，会默认以这个类名的小写为表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer)
    articleid = db.Column(db.Integer)
    comment=db.Column(db.Text)
    create_time = db.Column(db.DateTime,server_default=func.now())

if __name__ =="__main__":
    db.create_all()






