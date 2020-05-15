from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from sqlalchemy import desc


class User(db.Model,UserMixin):
  '''
  this has the characteristics of a user
  '''
  __tablename__ = "users"

  id = db.Column(db.Integer, index = True,primary_key = True)
  identification = db.Column(db.Integer,unique = True, index = True)
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True, index = True)
  Address = db.Column(db.String())
  pass_secure = db.Column(db.String(255))
  contactNumber = db.Column(db.String(),unique = True)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  payment_name = db.Column(db.String,db.ForeignKey('payment.name'))
  orders = db.relationship('Orders',backref = 'order', lazy = 'dynamic')
  receipients = db.relationship('Receipient',backref = 'receipient', lazy = 'dynamic')
  @property
  def password(self):
    raise AttributeError('You cannot access the password attribute')

  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

  @login_manager.user_loader
  def load_user(user_id):
    '''
    call back function that returns a user when unique identifier is passed
    '''
    return User.query.get(int(user_id))

class PaymentMethod(db.Model):
  '''
  this will have the preferred payment option per user
  '''

  __tablename__ = "payment"

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255),unique = True)
  users = db.relationship('User',backref = 'payment', lazy = 'dynamic')

class Orders(db.Model):

  '''
  this will be the attributes of an order
  '''
  __tablename__ = "orders"

  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  weight = db.Column(db.String())
  zone = db.Column(db.String(), db.ForeignKey('zones.name'))
  destination = db.Column(db.String(255))
  token = db.Column(db.String(255),unique = True, index = True)
  totalprice = db.Column(db.Integer())
  ParcelTypename = db.Column(db.String, db.ForeignKey('parcel.name'))
  DeliveryTypename = db.Column(db.String, db.ForeignKey('delivery.name'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.identification'))
  deliveryStatus = db.Column(db.String())
  NumberOfItem  = db.Column(db.Integer())

  def save_order(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_order_by_token(cls,tokenid):

    singleorder = Orders.query.filter_by(token = tokenid).first()

    return singleorder

  def get_all_orders():
    orderlist = Orders.query.order_by(desc(Orders.id)).all()

     

    return orderlist

  @classmethod
  def get_order_by_userID(cls,userID):
    orderlist = Orders.query.filter_by(user_id = userID)

    return orderlist


class Zones(db.Model):
  '''
  this will be some of the areas we deliver to and the cost
  '''
  __tablename__ = "zones"
  
  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True )
  cost = db.Column(db.Integer)
  orders = db.relationship('Orders',backref = 'zones', lazy = 'dynamic')

class DeliveryType(db.Model):
  '''
  this defines whether the parcel will choose express delivery or normal
  '''
  __tablename__ = "delivery"
  
  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True)
  orders = db.relationship('Orders',backref = 'deliveryT', lazy = 'dynamic')

class Roles(db.Model):
  '''
  this has the different roles of a logged in user, Admin or Client
  '''
  __tablename__ = "roles"

  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True)
  users = db.relationship('User', backref = 'role', lazy = 'dynamic')

class ParcelType(db.Model):
  '''
  type of parcel, whether the parcel is fragile, a perishable, or none
  '''
  __tablename__ = "parcel"

  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True)
  cost = db.Column(db.Integer())
  orders = db.relationship('Orders',backref = 'parcelT', lazy = 'dynamic')

class Receipient(db.Model):

  '''
  this has the characteristics of a receipient
  '''
  __tablename__ = "receipient"

  id = db.Column(db.Integer, index = True,primary_key = True)
  identification = db.Column(db.Integer,unique = True, index = True)
  FullName = db.Column(db.String(255))
  contact = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True, index = True)
  user_id = db.Column(db.Integer,db.ForeignKey('users.identification'))

  @classmethod
  def get_receipient(cls,userid):
    newRecepient = Receipient.query.filter_by(user_id = userid).first()
    return newRecepient