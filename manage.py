from app import create_app
from flask_script import Manager,Server
from app.models import User,PaymentMethod,ParcelType,Order,Zones,DeliveryType,Roles
from app import db
from flask_migrate import Migrate,MigrateCommand

#creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)
@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User = User,PaymentMethod = PaymentMethod,
  ParcelType = ParcelType,Order = Order,Zones = Zones,DeliveryType = DeliveryType,Roles = Roles )


if __name__ == '__main__':
  manager.run()