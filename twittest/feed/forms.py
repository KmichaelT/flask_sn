from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class FeedsForm(FlaskForm):
    
    title = StringField('Title', validators=[DataRequired()],render_kw={"placeholder": "Title"})
    text = TextAreaField('Text', validators=[DataRequired()],render_kw={"placeholder": "Text..."})
    submit = SubmitField('Post')
