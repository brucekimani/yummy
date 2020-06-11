from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    pitch = TextAreaField('Your Order', validators=[Required()])
    # my_menu = StringField('Menu', validators=[Required()])
    my_menu = SelectField('Menu', choices=[('Large'),('Medium'),('Small')],validators=[Required()])
    submit = SubmitField('Make Your Order!')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about our services',validators=[Required()])
    submit = SubmitField('Submit')