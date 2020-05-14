
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,IntegerField
from wtforms.validators import Required

class ParcelOrderForm(FlaskForm):

    weight = IntegerField('Weight')
    zone = StringField('Zone')
    destination = StringField('Destination')
    ParcelTypeName = StringField('ParcelTypeName')
    ParcelTypeName = SelectField('Parcel Category', choices=[('Perishable', 'Perishable'), ('non Perishable', 'non Perishable'), ('Fragile','Fragile'),(' non Fragile', 'non Fragile')])
    submit = SubmitField('Next')
    