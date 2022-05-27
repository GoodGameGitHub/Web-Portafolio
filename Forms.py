from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets import TextArea

class ContactMeForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=5,max=40)]);
    email = StringField('Email',validators=[DataRequired(), Email()]);
    subject = StringField('Subject',validators=[DataRequired(), Length(min=2,max=100)]);
    message = StringField('Message',widget=TextArea(),validators=[DataRequired()]);
    

class CommentForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(min=5,max=40)]);
    email = StringField('Email',validators=[DataRequired(), Email()]);
    comment = StringField('Comment',validators=[DataRequired()]);