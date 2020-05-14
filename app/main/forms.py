
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,IntegerField
from wtforms.validators import Required

class ParcelOrderForm(FlaskForm):

    
    weight = SelectField('Weight', choices=[('less than 1kg','less than 1kg'),('between 1kg and 2kg','between 1kg and 2kg'),('between 2.1kg and 3kg','between 2.1kg and 3kg')])
    #zone = SelectField('Zone', choices=[('south C', 'south C'), ('south B', 'south B'), ('south A','south A'),(' south D', 'south D'),('Other', 'Other')])
   # destination = StringField('Destination',)
    ParcelTypeName = StringField('ParcelTypeName')
    ParcelTypeName = SelectField('Parcel Category', choices=[('Perishable', 'Perishable'), ('non Perishable', 'non Perishable'), ('Fragile','Fragile'),(' non Fragile', 'non Fragile')]) 
    NumberOfItem = SelectField('Number Of Item' , choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')])
    submit = SubmitField('Next')
    

class UpdateParcelForm(FlaskForm):

    location = StringField('Parcel current location')
    submit = SubmitField('Next')

