
from datetime import datetime
from flask import current_app
from flaskblog import db,login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as Serializer
from flaskblog import admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flaskblog import admin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)




    def get_reset_token(self):
        s=Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'usr_id':self.id})

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id=s.loads(token['usr_id'])
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"




class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class UserAdmin(ModelView):
    column_list=("username","email","img_file","password")
    column_labels=("username","email","img_file","password")
    
    def is_accessible(self):
        return current_user.is_authenticated 
    
class PostAdmin(ModelView):
    column_list=('title','date_posted','content')
    column_labels=('title','date_posted','content')
    def is_accessible(self):
        return current_user.is_authenticated 

# admin.add_view(ModelView(Admin,db.session))
# admin.add_view(ModelView(Post,db.session))
