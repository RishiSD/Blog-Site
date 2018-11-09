from flask_mongoengine.wtf import model_form
from wtforms import validators

from FlaskBlogApp import db


class Posts(db.Document):
    title = db.StringField(max_length=150,
                           validators=[validators.InputRequired()])
    subtitle = db.StringField(max_length=200,
                              validators=[validators.InputRequired()])
    author = db.StringField(max_length=50,
                            validators=[validators.InputRequired()])
    content = db.StringField(validators=[validators.InputRequired()])
    date_posted = db.DateTimeField()


PostForm = model_form(Posts, field_args={'content': {'textarea': True}})
