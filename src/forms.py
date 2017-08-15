from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class CarForm(FlaskForm):
    """Form for adding new car"""
    plate = StringField('plate', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])

    def validate(self):
        """Additional validation goes here"""
        if not FlaskForm.validate(self):
            return False
        return True

