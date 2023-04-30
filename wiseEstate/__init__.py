from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_URI
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 开启输出底层执行的sql语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 开启数据库的自动提交功能[一般不使用]
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
    db.init_app(app)

    from auth_module.models.user import User
    return app

def create_database(app):
    db.create_all(app=app)
    print('create databae')