from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

    def get_id(self):
        return self.uid

    def __repr__(self):
        return f'Пользователь: {self.username}, uid: {self.uid}'