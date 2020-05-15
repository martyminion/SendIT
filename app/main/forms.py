
from flask_wtf import FlaskForm
from wtforms.validators import Required
from ..models import DeliveryType,Zones
from wtforms import ValidationError
from wtforms import StringField,StringField,IntegerField,SubmitField,BooleanField,ValidationError,SelectField


class DestinationForm(FlaskForm):
    destination= SelectField('Parcel Destination', choices=[('nakuru to nairobi','nairobi to naivasha'),('narobi to mombasa','narobi to mombasa'),('nairobi to eldoret','nairobi to eldoret')])
    deliverytype = SelectField('Delivery type', choices=[('express','express'),('normal','normal')])
    submit = SubmitField("Next")

class ParcelOrderForm(FlaskForm):
    weight = SelectField('Weight', choices=[('less than 1kg','less than 1kg'),('between 1kg and 2kg','between 1kg and 2kg'),('between 2.1kg and 3kg','between 2.1kg and 3kg'),("heavier than 3kg","heavier than 3kg")])
    ParcelTypeName = SelectField('Parcel Category', choices=[('Perishable', 'Perishable'), ('non Perishable', 'non Perishable'), ('Fragile','Fragile'),('non Fragile', 'non Fragile')]) 
    NumberOfItem = SelectField('Number Of Item' , choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')])
    submit = SubmitField('Next')
    
class UpdateParcelForm(FlaskForm):
    location = StringField('Parcel current location')
    delivery = StringField('Parcel Delivery Status')
    submit = SubmitField('Done')

class ReceipientForm(FlaskForm):
    FullName = StringField('Receipients Full Name',validators=[Required()])
    contact = StringField('Receipients Phone NUmber',validators=[Required()])
    email = StringField('Receipients email',validators=[Required()])
    identification = IntegerField('Receipients ID number or Passport Number',validators=[Required()])
    submit = SubmitField("Add Receipient")