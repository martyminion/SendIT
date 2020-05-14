from . import main
from flask import render_template,request,url_for,flash

from . import main
from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from ..models import DeliveryType,Zones

from .. import db

from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import DestinationForm
from .. import db



@main.route('/destination/<userid>/',methods = ["GET","POST"])
def destination(userid):
    '''
    View Function to register new users
    '''

    form = DestinationForm()
    Zones = Orders.query.filter_by().first()
    cost = 500
    if form.validate_on_submit():
            #check the parcelorder destination
                if form.destination.data == "nairobi to naivasha":
                 cost = cost + 200 

                elif form.destination.data == "narobi to mombasa":
                 cost = cost + 500

                elif form.destination.data == 'nairobi to eldoret':
                 cost = cost + 800

                else:
                 flash("Please choose a valid option")
                #check the parcel order type
                if form.deliverytype == "urgent":
                 cost = cost + 800

                elif form.deliverytype == " normal":
                 cost =  cost + 200


    new_order = Orders( destination= form.destination.data,  deliverytype= DestinationForm.deliverytype.data,totalprice = cost)
    
    new_order.save_order()

    
    
    return render_template('destination.html',destination_form = form)