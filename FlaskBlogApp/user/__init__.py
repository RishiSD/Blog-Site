from flask_mongoengine.wtf import model_form
from wtforms import validators

from FlaskBlogApp import db


class User(db.Document):
    username = db.StringField(required=True, max_length=50,
                              validators=[validators.InputRequired()])
    password = db.StringField(required=True,
                              validators=[validators.InputRequired()])
    authenticated = db.BooleanField()

    def is_active(self):
        return True

    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    @classmethod
    def get_user_by_username(cls, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        else:
            return user


UserForm = model_form(User, field_args={'password': {'password': True}})
