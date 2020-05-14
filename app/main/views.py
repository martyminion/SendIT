from . import main
from flask import render_template,request,url_for,flash,redirect
from .. import db

from ..email import mail_message

from ..tokengenerator import autogenerate_token
from .forms import ParcelOrderForm, UpdateParcelForm



@main.route('/')
def index():

  return render_template('index.html')

@main.route('/mailtest/')
def test_email_parameters():
  
  mail_message("This is your receipt","email/receipt","martkimwaweru@gmail.com")
  return redirect(url_for('main.index'))

@main.route('/mailtest/moreparams')
def test_email_parameters2():
  
  mail_message("Your parcel number 123","email/order","martkimwaweru@gmail.com")
  

  return redirect(url_for('main.index'))

@main.route('/ParcelOrder')
def Order():

  form = ParcelOrderForm()
  return render_template('ParcelOrder.html', title='Create a Parcel Order', form=form)

@main.route('/Admin/Update_Parcel/')
def update_parcel():

  form = UpdateParcelForm()

  if form.validate_on_submit():
    order.destination = form.destination.data

    db.session.add(new_location)
    db.session.commit()

    mail_message("Parcel location update","email/update_parcel",user.email,user=user)

    return redirect(url_for('main.update_parcel'))

  return render_template('index.html', title = 'Current location of the parcel' )

  