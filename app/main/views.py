from . import main
from flask import flash,render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required
from ..models import User,DeliveryType,Zones,Orders,Receipient
from ..email import mail_message
from ..tokengenerator import autogenerate_token
from .forms import ParcelOrderForm, UpdateParcelForm,DestinationForm,ReceipientForm
from .. import db


@main.route('/')
def index():
  title = "SendIT"
  return render_template('index.html',title = title)

@main.route('/confirm/<tokenid>/<userID>',methods = ['GET','POST'])
def confirm_order(tokenid,userID):
  flash("Order Confirmed Successfully")
  orderdets = Orders.get_order_by_token(tokenid)
  orderdets.deliveryStatus = "Client Confirmed"
  db.session.commit()
  user = User.query.filter_by(identification = userID).first()
  mail_message("This is your receipt","email/receipt",user.email,user = user,orderdets = orderdets)
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
    new_token = autogenerate_token(5)
    new_order = Orders(weight = form.weight.data, token = new_token, ParcelTypename = form.ParcelTypeName.data,NumberOfItem = form.NumberOfItem.data, user_id = user.identification,totalprice = cost)
    
    new_order.save_order()

    return redirect(url_for('main.destination', newtoken = new_token))

  return render_template('ParcelOrder.html', title='Create a Parcel Order', form=form )

@main.route('/<newtoken>/destination/',methods = ["GET","POST"])
@login_required
def destination(newtoken):
    form = DestinationForm()
    new_order = Orders.query.filter_by(token = newtoken).first()
    if form.validate_on_submit():
      new_order.destination = form.destination.data
      new_order.DeliveryTypename = form.deliverytype.data
      
      return redirect(url_for('main.singleorder', token = new_order.token))
  
    return render_template('destination.html',destination_form = form)


@main.route('/Admin/<tokenid>/Update_Parcel',methods = ['GET','POST'])
@login_required
def update_parcel(tokenid):

  form = UpdateParcelForm()
  orderdets = Orders.query.filter_by(token = tokenid).first()

  if form.validate_on_submit():
    location = form.destination.data
    orderdets.destination = location
    db.session.commit()

    mail_message("Parcel location update","email/update",user.email,user=user,orderdets = orderdets)
    if Receipient.get_receipient(orderdets.user_id):
      mailreceipt = Receipient.get_receipient(orderdets.user_id)
      mail_message("Parcel location update","email/update",mailreceipt.email,user=user,orderdets = orderdets)
    return redirect(url_for('main.allorders'))

  return render_template('update_parcel.html', title = 'Current location of the parcel',form = form )

@main.route('/order/<token>/details')
@login_required
def singleorder(token):
  single_order = Orders.get_order_by_token(token)
  title = "Single Order"
  return render_template('singleorder.html',single_order = single_order)

@main.route('/all/orders')
@login_required
def allorders():
  order_list = Orders.get_all_orders()

  title = 'All Orders'

  return render_template('allorders.html', order_list = order_list)

@main.route('/<userID>/orders')
@login_required
def alluserOrders(userID):
  orderlist = Orders.get_order_by_userID(userID)

  return render_template('clientorders.html',orderlist = orderlist)
  
@main.route('/<token>/cancel/order')
@login_required
def cancel_order(token):
  cancelorder = Orders.get_order_by_token(token)

  cancel_order.deliveryStatus = "Client Cancelled"
  db.session.commit()

  return redirect(url_for('main.singleorder',token = token))

@main.route('/<tokenid>/<userid>/receipient',methods = ['GET','POST'])
def receipientdetails(tokenid,userid):
  user = User.query.filter_by(identification = userid).first()
  orderdets = Orders.get_order_by_token(tokenid)
  form = ReceipientForm()

  if form.validate_on_submit():
    new_recipient = Receipient(identification = form.identification.data,FullName = form.FullName.data,contact = form.contact.data,email = form.email.data,user_id = user.identification)
    db.session.add(new_recipient)
    db.session.commit()

    return redirect(url_for('main.singleorder',token = tokenid)) 

  return render_template('receipientform.html',form = form, title = "Add receipient")