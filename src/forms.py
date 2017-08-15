from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,\
    BooleanField, SubmitField
from wtforms.validators import DataRequired


class CarForm(FlaskForm):
    """Form for adding new car"""
    plate = StringField('rejestracja', validators=[DataRequired()])
    description = StringField('opis', validators=[DataRequired()])

    def validate(self):
        """Additional validation goes here"""
        if not FlaskForm.validate(self):
            return False
        return True


class LoginForm(FlaskForm):
    username = StringField('Użytkownik', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Pozostań zalogowany')
    submit = SubmitField('Zaloguj')
