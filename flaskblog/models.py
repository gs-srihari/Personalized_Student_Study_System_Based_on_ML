from flaskblog import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):

        return f"User('{self.username}', '{self.email}')"





class Usage(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    nosessions = db.Column(db.Integer, nullable=False)
    def __repr__(self):

        return f"Post('{self.username}', '{self.nosessions}')"

class Performanceval(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    performance = db.Column(db.String(20), nullable=False)
    def __repr__(self):

        return f"Post('{self.username}', '{self.performance}')"