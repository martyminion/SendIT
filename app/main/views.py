from . import main
from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User,DeliveryType,Zones,Orders
from ..email import mail_message
from ..tokengenerator import autogenerate_token
from .forms import ParcelOrderForm, UpdateParcelForm,DestinationForm
from .. import db

@main.route('/destination/',methods = ["GET","POST"])
def destination():
    form = DestinationForm()
    if form.validate_on_submit():
      pass
  
    return render_template('destination.html',destination_form = form)

@main.route('/')
def index():
  title = "SendIT"
  return render_template('index.html',title = title)

@main.route('/services')
def services():
  title = "Services"
  return render_template('services.html',title = title)

@main.route('/mailtest/')
def test_email_parameters():
  
  mail_message("This is your receipt","email/receipt","martkimwaweru@gmail.com")
  return redirect(url_for('main.index'))

@main.route('/mailtest/moreparams')
def test_email_parameters2():
  
  mail_message("Your parcel number 123","email/order","martkimwaweru@gmail.com")
  

  return redirect(url_for('main.index'))

@main.route('/<userid>/ParcelOrder/',methods = ['GET','POST'])
@login_required
def Order(userid):
  user = User.query.filter_by(identification = userid).first()
  cost = 200
  form = ParcelOrderForm()
  if form.validate_on_submit():
    #check the parcelorder weight
    if form.weight.data == "less than 1kg":
      cost = cost + 500 

    elif form.weight.data == "between 1kg and 2kg":
      cost = cost + 1000

    elif form.weight.data == "between 2.1kg and 3kg":
      cost = cost + 1500

    elif form.weight.data == "heavier than 3kg":
      cost = cost + 2000
    else:
      flash("Please choose a valid option")
    #check the parcel order type
    if form.ParcelTypeName == "Perishable":
      cost = cost + 800
    
    elif form.ParcelTypeName == " non Perishable":
      cost =  cost + 200

    elif form.ParcelTypeName == "Fragile":
      cost = cost + 1000

    elif form.ParcelTypeName == "non Fragile":
      cost = cost + 200

    new_order = Orders(weight = form.weight.data, token = autogenerate_token(5), ParcelTypename = form.ParcelTypeName.data,NumberOfItem = form.NumberOfItem.data, user_id = user.identification,totalprice = cost)
    
    new_order.save_order()

    redirect(url_for('main.destination'))

  return render_template('ParcelOrder.html', title='Create a Parcel Order', form=form)

@main.route('/Admin/<tokenid>/Update_Parcel')
def update_parcel(tokenid):

  form = UpdateParcelForm()
  orderdets = Orders.query.filter_by(token = tokenid).first()

  if form.validate_on_submit():
    location = form.destination.data
    orderdets.destination = location
    db.session.commit()

    mail_message("Parcel location update","email/update_parcel",user.email,user=user)

    return redirect(url_for('main.update_parcel'))

  return render_template('index.html', title = 'Current location of the parcel' )

  

