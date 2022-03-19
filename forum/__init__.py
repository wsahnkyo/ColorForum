from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from .models import *  # 需要导入，且放在db下面，因为models文件中需要引入db,from . import db
# from .views import account
from forum.color import color
from forum.login import login
from flask import Flask
from forum.article import article
from forum.information import information
from forum.forum import forum
from forum.home import home
import configs




def create_app():
    app = Flask(__name__)
    app.config.from_object(configs.Config)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    # 将db注册到app中
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(article, url_prefix='/article')
    app.register_blueprint(color, url_prefix='/color')
    app.register_blueprint(login, url_prefix='/login')
    app.register_blueprint(information, url_prefix='/information')
    app.register_blueprint(forum, url_prefix='/forum')
    app.register_blueprint(home, url_prefix='/')
    return app