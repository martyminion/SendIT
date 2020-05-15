from . import auth
from flask import render_template,request,url_for,flash,abort,redirect
from .. import db
from flask_login import login_required,current_user,login_user,logout_user
from .forms import LoginForm,ClientRegistrationForm,AdminRegistrationForm
from ..models import User

@auth.route('/login', methods = ['GET','POST'])
def login():
  login_form = LoginForm()
  
  if login_form.validate_on_submit():
    user = User.query.filter_by(email = login_form.email.data).first()
    if user is None:
      flash("This email has no account with us")
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user)
      return redirect(request.args.get('next') or url_for('main.index'))
  title = "Login"
  return render_template('auth/login.html',title = title, login_form = login_form)

@auth.route('/<adminid>/register/newAdmin', methods = ['GET','POST'])
@login_required
def regiser_new_admin(adminid):
  user = User.query.filter_by(identification = adminid).first()
  
  if user.role_id is not 1:
    abort(404)
  if user.role_id is 1:
    Admin_reg_form = AdminRegistrationForm()
    if Admin_reg_form.validate_on_submit():
      new_admin = User(identification = Admin_reg_form.identification.data,
      firstName = Admin_reg_form.firstName.data, lastName =Admin_reg_form.lastName.data,
       email=Admin_reg_form.email.data, Address = Admin_reg_form.address.data,
      role_id = 1, password = Admin_reg_form.password.data)

      db.session.add(new_admin)
      db.session.commit()
      flash("Added new Admin User")

      return redirect(url_for('auth.login'))
  title = 'Register Admin'

  return render_template('auth/AdminRegister.html',title = title, Admin_reg_form = Admin_reg_form)

@auth.route('/register/client', methods = ['GET','POST'])
def regiser_cleint():
  Client_reg_form = ClientRegistrationForm()
  if Client_reg_form.validate_on_submit():
      new_client = User(identification = Client_reg_form.identification.data,
      firstName = Client_reg_form.firstName.data, lastName =Client_reg_form.lastName.data,
      email=Client_reg_form.email.data, Address = Client_reg_form.address.data,
      role_id = 2, payment_name = Client_reg_form.payment.data, password = Client_reg_form.password.data)

      db.session.add(new_client)
      db.session.commit()
      return redirect(url_for('auth.login'))

  title = 'Register Client'

  return render_template('auth/Register.html',title = title, Client_reg_form = Client_reg_form)

@auth.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))