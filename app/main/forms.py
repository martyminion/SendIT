
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,SelectField,IntegerField
from wtforms.validators import Required
class ParcelOrderForm(FlaskForm):

    id = IntegerField('id')
    weight = IntegerField('Weight')
    Zone = TextAreaField('Zone')
    destination = TextAreaField('Destination')
    token = TextAreaField('Token')
    totalprice = IntegerField('Totalprice')
    ParcelTypeName = TextAreaField('ParcelTypeName')
    user_id = IntegerField('user_id')
    deleveryStatus = TextAreaField('deleveryStatus')
    ParcelTypeName = SelectField(u'Parcel Category', choices=[('Perishable', 'Perishable'), ('non Perishable', 'non Perishable'), ('Fragile','Fragile'),(' non Fragile', 'non Fragile')])
    submit = SubmitField('Submit')
    ***********
    7777