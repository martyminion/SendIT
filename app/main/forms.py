from flask_wtf import FlaskForm

from wtforms.validators import Required
from ..models import DeliveryType,Zones
from wtforms import ValidationError
from wtforms import StringField,StringField,IntegerField,SubmitField,BooleanField,ValidationError,SelectField
from wtforms.validators import Required




class DestinationForm(FlaskForm):
    destination= SelectField('Parcel Destination', choices=[('nakuru to nairobi','nairobi to naivasha'),('narobi to mombasa','narobi to mombasa'),('nairobi to eldoret','nairobi to eldoret')])
    
  
    deliverytype = SelectField('delivery type', choices=[('urgent','urgent'),('normal','normal')])
    
    submit = SubmitField("Submit")


    # def validate_email(self,data_field):
    #     if User.query.filter_by(email = data_field.data).first():
    #         raise ValidationError('There is an account with that email.')

    # def validate_username(self,data_field):
    #     if User.query.filter_by(username = data_field.data).first():
    #         raise ValidationError('That username is taken.')



