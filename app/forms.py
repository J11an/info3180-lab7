from flask_wtf import FlaskForm
from wtforms import FileField,TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired,FileAllowed

class UploadForm(FlaskForm):

    description = TextAreaField('description',validators =[InputRequired()])
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg','png'],'Images')])



