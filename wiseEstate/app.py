from flask import Flask
from database import db
from config import DB_URI
from auth_module.models.user import User


app = Flask(__name__,static_url_path='/')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 开启输出底层执行的sql语句
app.config['SQLALCHEMY_ECHO'] = True

# 开启数据库的自动提交功能[一般不使用]
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()