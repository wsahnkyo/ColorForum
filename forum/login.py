# coding:utf-8
from  mapping import  User,Article
from flask import session
from flask import Blueprint, render_template, request

import json
from forum import db, global_config
login = Blueprint('login', __name__)



@login.route("/",methods=['GET','POST'])
def loginPage():

    return render_template('login.html',WEBREF=global_config.WEBREF)

@login.route("/homepage",methods=['GET','POST'])
def homepage():
     username = request.form.get("username")
     pasword = request.form.get("password")
     count = User.query.filter(User.username == f'{username}').filter(User.password == f'{pasword}').count()
     dict = {"1": "黑色系", "2": "蓝色系", "3": "黄色系", "4": "绿色系", "5": "水色系", "6": "红色系", "7": "苍色系", "8": "灰白色系",
             "9": "金银色系", "10": "紫色系"}
     if request.method == 'POST':
         if count!=1:
          message='用户名或密码错误'
          return   render_template('error.html',WEBREF=global_config.WEBREF,message=message,dict=dict)
         else:
             # user2 = db.session.query(User.id, User.username, User.password).filter(User.username == f'{user}').filter(User.password == f'{pasword}')
             # print(user2)
             # with open("../data.txt", "w") as f:
             #     f.write(str(user2[0].id))
             user = User.query.filter(User.username == f'{username}').filter(User.password == f'{pasword}').one()
             session['id'] =user.id
             return render_template('home.html',dict=dict)

     else:
         return render_template('home.html',dict=dict)




@login.route("/registerPage",methods=['GET','POST'])
def registerPage():
    return render_template('registerPage.html',WEBREF=global_config.WEBREF)


@login.route("/register",methods=['GET','POST'])
def register():
    data = request.get_data()
    data = json.loads(data)
    username = data['username']
    password = data['password']

    user = User(username=f'{username}',password=f'{password}')
    db.session.add(user)
    db.session.commit()
    return json.dumps({'status': '0', 'errmsg': '注册成功！'}, ensure_ascii=False)


@login.route("/outLogin",methods=['GET','POST'])
def outLogin():
    dict = {"1": "黑色系", "2": "蓝色系", "3": "黄色系", "4": "绿色系", "5": "水色系", "6": "红色系", "7": "苍色系", "8": "灰白色系",
            "9": "金银色系", "10": "紫色系"}
    session.clear()
    return render_template('home.html',WEBREF=global_config.WEBREF,dict=dict)

