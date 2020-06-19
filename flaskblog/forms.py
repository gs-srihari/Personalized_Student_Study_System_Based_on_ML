from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,SelectField,FloatField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.Please choose a different one')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken.Please choose a different one')

class UserProfileForm(FlaskForm):
    Institution = StringField('Institution',validators=[DataRequired()])
    State = SelectField('State',choices =[("A","Andhra Pradesh"),("B","Arunachal Pradesh"),("C","Assam"),("D","Bihar"),("E","Chhattisgarh"),("F","Goa"),("G","Gujarat"),("H","Haryana"),("I","Himachal Pradesh"),("J","Jammu and Kashmir"),("K","Jharkhand"),("L","Karnataka"),("M","Kerala"),("N","Madhya Pradesh"),("O","Maharashtra"),("P","Manipur"),("Q","Meghalaya"),("R","Mizoram"),("S","Nagaland"),("T","Odisha"),("V","Punjab"),("W","Rajasthan"),("X","Sikkim"),("Y","Tamil Nadu"),("Z","Telangana"),("AA","Uttar Pradesh"),("AB","West Bengal")])
    Gender = SelectField('Gender',choices =[("A","Male"),("B","Female")])
    Marks_10th=FloatField('10th Percentage',validators=[DataRequired()])
    Year_10th=IntegerField('Year of 10th completion',validators=[DataRequired()])
    Marks_12th=FloatField('12th Percentage',validators=[DataRequired()])
    Year_12th=IntegerField('Year of 12th completion',validators=[DataRequired()])
    Degree=SelectField('Degree of Study',choices=[("X","B.Tech"),("W","M.Tech"),("Y","B.Sc"),("Z","M.Sc")])
    Specialisation=SelectField('Specialisation',choices=[("A","Minors CSE"),("B","CSE"),("C","CSE With AI"),("D","CSE With CPS"),("E","Majors CSE")])
    College_Percent=FloatField('College Percentage',validators=[DataRequired()])
    Age=IntegerField('Age',validators=[DataRequired()])
    English_Test_1=FloatField('English Test 1',validators=[DataRequired()])
    English_Test_2=FloatField('English Test 2',validators=[DataRequired()])
    English_Test_3=FloatField('English Test 3',validators=[DataRequired()])
    English_Test_4=FloatField('English Test 4',validators=[DataRequired()])
    Quants_1=FloatField('Quantitative Test 1',validators=[DataRequired()])
    Quants_2=FloatField('Quantitative Test 2',validators=[DataRequired()])
    Quants_3=FloatField('Quantitative Test 3',validators=[DataRequired()])
    Quants_4=FloatField('Quantitative Test 4',validators=[DataRequired()])
    Domain_1=FloatField('Domain Test 1',validators=[DataRequired()])
    Domain_2=FloatField('Domain Test 2',validators=[DataRequired()])
    Domain_3=FloatField('Domain Test 3',validators=[DataRequired()])
    Domain_4=FloatField('Domain Test 4',validators=[DataRequired()])
    Analytics_1=FloatField('Analytical Skills 1',validators=[DataRequired()])
    Analytics_2=FloatField('Analytical Skills 2',validators=[DataRequired()])
    Analytics_3=FloatField('Analytical Skills 3',validators=[DataRequired()])
    submit=SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')

