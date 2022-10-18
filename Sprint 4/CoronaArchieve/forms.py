from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TimeField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from CoronaArchieve.models import Visitor, Place

# flask form for visitor registration


class RegistrationForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone_number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_id(self, id):
        visitor = Visitor.query.filter_by(id=id.data).first()
        if visitor:
            raise ValidationError('Visitor Id already registered.')

# flask form for place registration


class PlaceRegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        place = Place.query.filter_by(place_username=username.data).first()
        if place:
            raise ValidationError('Username Taken.')

# flask form for agent to add hospital


class AddHospitalForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[
                                     DataRequired(), EqualTo('password')])
    add = SubmitField('Add')


# flask form for visitor to login
class VisitorsLoginForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')

# flask form places to login


class PlaceLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')

# flask form for hospital login


class HospitalLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')

# flask form for agent to login


class AgentLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')

# flask form for agent to search for visitors


class AgentSearchForVisitorForm(FlaskForm):
    PlaceName = StringField('PlaceName', validators=[DataRequired()])
    DateTime = TimeField('Date', validators=[DataRequired()])
    StartTime = DateField('Time')
    EndTime = DateField('Time')
    Search = SubmitField('SearchForPeople')


class AgentSearchForPlaceForm(FlaskForm):
    PeopleName = StringField('PeopleName', validators=[DataRequired()])
    DateTime = TimeField('Date', validators=[DataRequired()])
    StartTime = DateField('Time')
    EndTime = DateField('Time')
    Search = SubmitField('SearchForPeople')
