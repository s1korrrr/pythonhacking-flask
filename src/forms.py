from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,\
    BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, \
    EqualTo, Email, ValidationError

from src.models import Owner


class CarForm(FlaskForm):
    """Form for adding new car"""
    plate = StringField('Nr rejestracji', validators=[DataRequired()])
    description = StringField('Nazwa auta', validators=[DataRequired()])

    def validate(self) -> bool:
        """Additional validation goes here"""
        if not FlaskForm.validate(self):
            return False
        return True


class LoginForm(FlaskForm):
    """Login form"""
    username = StringField('Użytkownik', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Pozostań zalogowany')
    submit = SubmitField('Zaloguj')


class SignInForm(FlaskForm):
    owner = StringField(
        'Użytkownik', validators=[
            DataRequired(), Length(3, 80),
            Regexp('^[A-Za-z0-9_]{3,}$',
                   message='Dopuszczalne litery, '
                           'cyfry oraz podkreślenia.')
        ]
    )
    email = StringField('Email', validators=[DataRequired(), Length(1, 120),
                                             Email()])
    password = PasswordField(
        'Hasło', validators=[
            DataRequired(),
            EqualTo('password2', message='Hasła muszą się zgadzać.')
        ]
    )
    password2 = PasswordField('Potwierdz hasło', validators=[DataRequired()])

    def validate_email(self, email_field):
        if Owner.query.filter_by(email=email_field.data).first():
            raise ValidationError('Adres email jest już zajęty.')

    def validate_owner(self, owner_field):
        if Owner.query.filter_by(email=owner_field.data).first():
            raise ValidationError('Użytkownik jest już zajęty.')
