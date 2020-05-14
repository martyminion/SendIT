from . import main
from flask import render_template,request,url_for,flash
from .. import db
from . import main
from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from ..models import DeliveryType,Zones
# from .forms import RegistrationForm
from .. import db
# from .forms import PitchForm
# from ..email import mail_message


# @main.route('/')
# def login():
#    return 'am ali'

# @main.route('/',methods = ["GET","POST"])
# def destination():
#     '''
#     View Function destination users
#     '''
    # form = DestinationForm
    # if form.validate_on_submit():
        
        # user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        # db.session.add(user)
        # db.session.commit()
        # return redirect(url_for('auth.login'))
    

    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     user = User(email = form.email.data, username = form.username.data,password = form.password.data)
    #     db.session.add(user)
    #     db.session.commit()

    #     flash("You've been successfully registered!")

    #     # mail_message("Welcome to My Blog","email/welcome_user",user.email,user=user)



    #     return redirect(url_for('auth.login'))

    # title = "Pitch-Perfect -- New Account"
    # return render_template('base.html' )#,DestinationForm = form)

from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import DestinationForm
from .. import db
# from ..email import mail_message


@main.route('/',methods = ["GET","POST"])
def register():
    '''
    View Function to register new users
    '''

    form = DestinationForm()
    if form.validate_on_submit():
        # user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        # db.session.add(user)
        # db.session.commit()

        flash("You've been successfully registered!")

        # mail_message("Welcome to My Blog","email/welcome_user",user.email,user=user)



     

    
    return render_template('destination.html',destination_form = form)

