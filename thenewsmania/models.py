from flask_login import UserMixin
from thenewsmania import LM, db

@LM.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    number=db.Column(db.String(10))
    notes=db.relationship('Note', backref='author')

    def __repr__(self):
        return f"User({self.username},{self.email},{self.id})"
class Note(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    content=db.Column(db.Text(), nullable=False)
    user_id=db.Column(db.Integer(), db.ForeignKey('user.id'))
