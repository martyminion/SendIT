from . import db

class User(db.Model):
  '''
  this has the characteristics of a user
  '''
  __tablename__ = "users"

  identification = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True, index = True)
  Address = db.Column(db.String())
  pass_secure = db.Column(db.String(255))
  contactNumber = db.Column(db.String())
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  payment_id = db.Column(db.Integer,db.ForeignKey('payment.id'))
  orders = db.relationship('Order',backref = 'order', lazy = 'dynamic')

class PaymentMethod(db.Model):
  '''
  this will have the preferred payment option per user
  '''

  __tablename__ = "payment"

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255),unique = True)
  users = db.relationship('User',backref = 'payment', lazy = 'dynamic')

class Order(db.Model):

  '''
  this will be the attributes of an order
  '''
  __tablename__ = "orders"

  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  weight = db.Column(db.Integer())
  zone = db.Column(db.String(), db.ForeignKey('zones.name'))
  destination = db.Column(db.String(255))
  token = db.Column(db.String(255),unique = True, index = True)
  totalprice = db.Column(db.Integer())
  ParcelTypeid = db.Column(db.Integer, db.ForeignKey('parcel.id'))
  DeliveryTypeid = db.Column(db.Integer, db.ForeignKey('delivery.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.identification'))
  deliveryStatus = db.Column(db.String())

class Zones(db.Model):
  '''
  this will be some of the areas we deliver to and the cost
  '''
  __tablename__ = "zones"
  
  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True )
  cost = db.Column(db.Integer)
  orders = db.relationship('Order',backref = 'zones', lazy = 'dynamic')

class DeliveryType(db.Model):
  '''
  this defines whether the parcel will choose express delivery or normal
  '''
  __tablename__ = "delivery"
  
  id = db.Column(db.Integer,unique = True, index = True, primary_key = True)
  name = db.Column(db.String(),unique = True)
  orders = db.relationship('Order',backref = 'deliveryT', lazy = 'dynamic')

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