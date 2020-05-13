from . import db


class User(db.Model):
  '''
  this has the characteristics of a user
  '''
  
  ___tablename__ = 'users'

  identification = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True, index = True)
  Address = db.Column(db.String())
  pass_secure = db.Column(db.String(255))
  contactNumber = db.Column(db.String())
  role_name = db.Column(db.String(), db.ForeignKey('roles.name'))
  payment_name = db.Column(db.String(),db.ForeignKey('payment.name'))
  ordersU = db.relationship('Order',backref = 'ordername', lazy = 'dynamic')

class PaymentMethod(db.Model):
  '''
  this will have the preferred payment option per user
  '''

  ___tablename__ = 'payment'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255),unique = True)
  users = db.relationship('User',backref = 'payment', lazy = 'dynamic')

class Order(db.Model):

  '''
  this will be the attributes of an order
  '''
  ___tablename__ = 'orders'

  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  weight = db.Column(db.Integer())
  zone = db.Column(db.String(), db.ForeignKey('zones.name'))
  destination = db.Column(db.String(255))
  token = db.Column(db.String(255),unique = True, index = True)
  totalprice = db.Column(db.Integer())
  ParcelTypeName = db.Column(db.String, db.ForeignKey('parcelType.name'))
  DeliveryTypeName = db.Column(db.String(), db.ForeignKey('deliverytype.name'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.identification'))
  deliveryStatus = db.Column(db.String())

class Zones(db.Model):
  '''
  this will be some of the areas we deliver to and the cost
  '''
  ___tablename__ = 'zones'
  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True )
  cost = db.Column(db.Integer)
  ordersZ = db.relationship('Order',backref = 'zones', lazy = 'dynamic')

class DeliveryType(db.Model):
  '''
  this defines whether the parcel will choose express delivery or normal
  '''
  ___tablename__ = 'deliverytype'
  
  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True)
  ordersD = db.relationship('Order',backref = 'delivery', lazy = 'dynamic')

class Roles(db.Model):
  '''
  this has the different roles of a logged in user, Admin or Client
  '''
  ___tablename__ = 'roles'

  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True)
  users = db.relationship('User', backref = 'role', lazy = 'dynamic')

class ParcelType(db.Model):
  '''
  type of parcel, whether the parcel is fragile, a perishable, or none
  '''
  ___tablename__ = 'parcelType'

  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True)
  cost = db.Column(db.Integer())
  ordersP = db.relationship('Order',backref = 'parcelT', lazy = 'dynamic')