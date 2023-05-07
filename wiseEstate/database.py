from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI  # Replace with your desired database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class UserAuth(db.Model):
    __tablename__ = 'user_auth'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(100))
    token = db.Column(db.String(255))
    token_expire = db.Column(db.DATETIME)
    
    def __repr__(self):
        return '<UserAuth %r>' % self.id

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(36), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    email_alternate = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address_id = db.Column(db.String(36), db.ForeignKey('address.id'), nullable=False)
    gender = db.Column(db.String(5))
    password_phrase = db.Column(db.String(100), nullable=False)
    register_ip = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(15), nullable=False)
    type = db.Column(db.String(15), nullable=False)
    avatar = db.Column(db.String(200))
    avatar_large = db.Column(db.String(200))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    note = db.Column(db.json)
    additional_info = db.Column(db.json)
    date_of_birth: db.Column(db.DATETIME)      
    customer_register_date: db.Column(db.DATETIME)


    def __repr__(self):
        return '<User %r>' % self.id

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)
    unit = db.Column(db.String(5), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    address = db.relationship('Address', backref='users')
    
    def __repr__(self):
        return '<Address %r>' % self.id
    
def create_database():
    db.create_all()
    print('Database initialized.')

if __name__ == '__main__':
    with app.app_context():
        # Drop the tables if they exist
        db.drop_all()

        # Create the tables
        db.create_all()
        create_database()