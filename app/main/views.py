from . import main
from flask import render_template,request,url_for,flash
from .. import db
from ..tokengenerator import autogenerate_token
from .forms import ParcelOrderForm


@main.route('/')
def index():
  
  return render_template('index.html')

@main.route('/ParcelOrder')
def Order():

  form = ParcelOrderForm()
  return render_template('ParcelOrder.html', title='Create a Parcel Order', form=form)
