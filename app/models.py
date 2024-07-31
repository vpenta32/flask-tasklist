from app import db

from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    events = db.relationship('Event', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Event {self.title}>'