from . import main
from flask import render_template,request,url_for,flash
from .. import db
from .forms import ParcelOrderForm



@main.route('/')
def index():
  
  return "<h1> ******you are a main login and testing braching ,MARTIN you can merge the Branch  *****</h1>"

@main.route('/ParcelOrder')
def Order():

  form = ParcelOrderForm()
  return render_template('ParcelOrder.html', title='Create a Parcel Order', form=form)
