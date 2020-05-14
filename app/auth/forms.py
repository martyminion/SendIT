from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, PasswordField,IntegerField
from wtforms.validators import Required,Email,EqualTo,email,ValidationError
from ..models import User

class LoginForm(FlaskForm):
  '''
  required login form fields
  '''
  email = StringField("Your Email Address", validators=[Required(),email()])
  password = PasswordField("Please Your Password",validators=[Required(), 
  EqualTo('password_confirm',message="These passwords do not match")])
  password_confirm = PasswordField("Confirm Password", validators=[Required()])
  submit = SubmitField('Welcome Back')

class AdminRegistrationForm(FlaskForm):
  '''
  required Client Registration fields
  ''' 
  identification = IntegerField("Please Enter ID number or Passport number", validators=[Required()])
  firstName = StringField('Please Enter First Name',validators=[Required()])
  lastName  = StringField('PLease Enter your Last Name',validators=[Required()])
  contactNumber = StringField("Please Enter your phone number",validators=[Required()])
  email = StringField('Please Enter Your Email Address',validators=[Required(),email()])
  address = StringField('Please enter Valid Address',validators=[Required()])
  password = PasswordField("Please Your Password",validators=[Required(), EqualTo('password_confirm',message="These passwords do not match")])
  password_confirm = PasswordField("Confirm Password", validators=[Required()])
  submit = SubmitField('Sign Up')


  def validate_email(self,data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError("There's an account with that email")

  def validate_identification(self,data_field):
    if User.query.filter_by(identification = data_field.data).first():
      raise ValidationError("There's an account with that identification Number")      
  
  def validate_contactNumber(self,data_field):
    if User.query.filter_by(contactNumber = data_field.data).first():
      raise ValidationError("There's an account with that Phone Number")      

class ClientRegistrationForm(FlaskForm):
  '''
  required admin Registration fields
  ''' 
  identification = IntegerField("Please Enter ID number or Passport number", validators=[Required()])
  firstName = StringField('Please Enter First Name',validators=[Required()])
  lastName  = StringField('Please Enter your Last Name',validators=[Required()])
  contactNumber = StringField("Please Enter your phone number",validators=[Required()])
  payment = SelectField("Preferred Payment type", choices=[("MPESA","MPESA"),("Debit Card","Debit Card")],validators=[Required()])
  email = StringField('Please Enter Your Email Address',validators=[Required(),email()])
  address = StringField('Please enter Valid Address',validators=[Required()])
  password = PasswordField("Please Your Password",validators=[Required(), EqualTo('password_confirm',message="These passwords do not match")])
  password_confirm = PasswordField("Confirm Password", validators=[Required()])
  submit = SubmitField('Sign Up')


  def validate_email(self,data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError("There's an account with that email")

  def validate_identification(self,data_field):
    if User.query.filter_by(identification = data_field.data).first():
      raise ValidationError("There's an account with that identification Number")      


