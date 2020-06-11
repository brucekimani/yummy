from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import text
import jwt
import os

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    hash_pass = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    profile_pic_path = db.Column(db.String(255))
    bio = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError("You can not read password attribute")
    
    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)
        
    def set_password(self, password):
        self.hash_pass = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)
    
    
    def __repr__(self):
        return f'User {self.username}'
    
    
class Pizza(db.Model):
    __tablename__ = 'pizza'
    
    id = db.Column(db.Integer, primary_key = True)
    pizza_contents = db.Column(db.String())
    pizza_category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    @classmethod
    def get_category(cls, cat):
        category = Pizza.query.filter_by(pizza_category = cat).order_by(text('-id')).all()
        
        return category        
    
class Comment(db.Model):
    __tablename__ = 'comments'
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    
    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pizza_id=id).all()
        return comments
    
    def __repr__(self):
        return f'{self.id_user}:{self.pitching_id}'
    
        
        