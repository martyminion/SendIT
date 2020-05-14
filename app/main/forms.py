from flask_wtf import FlaskForm

from wtforms.validators import Required
from ..models import DeliveryType,Zones
from wtforms import ValidationError
from wtforms import StringField,StringField,IntegerField,SubmitField,BooleanField,ValidationError,SelectField
from wtforms.validators import Required




class DestinationForm(FlaskForm):
    destination= SelectField('Parcel Destination', choices=[('nakuru to nairobi','nairobi to naivasha'),('narobi to mombasa','narobi to mombasa'),('nairobi to eldoret','nairobi to eldoret')])
    
    # destinationwave= SelectField('Parcel Destination', choices=[('nakuru to nairobi','nairobi to naivasha'),('narobi to mombasa','narobi to mombasa'),('nairobi to eldoret','nairobi to eldoret')])
    username = StringField("Enter the name of the estate",validators=[Required()])
    deliverytype = SelectField('Delivery type', choices=[('urgent','urgent'),('normal','normal')])
    
    submit = SubmitField("Submit")




