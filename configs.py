class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://train:train@localhost:3306/forum?autocommit=1' #用于连接数据的数据库。
    SQLALCHEMY_TRACK_MODIFICATIONS = True #如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_ECHO = True  #如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。
    SQLALCHEMY_POOL_SIZE = 50
