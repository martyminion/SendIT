from . import main
from flask import render_template,request,url_for,flash,redirect
from .. import db
from ..email import mail_message


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