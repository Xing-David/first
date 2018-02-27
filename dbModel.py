from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# DATABASE_URI = os.environ.get('DATABASE_URI')
DATABASE_URI = 'postgres://etanvgnlopdhfw:5166e1c5d397e5f0a2d9a9493f3655deb047a20c0be19d22d84b85d00c9d87b8@ec2-174-129-26-203.compute-1.amazonaws.com:5432/d48sp3dtdg4fao'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class UserData(db.Model):
    __tablename__ = 'UserData'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Description = db.Column(db.String(256))
    CreateDate = db.Column(db.DateTime)

    def __init__(self
                 , Name
                 , Description
                 , CreateDate
                 ):
        self.Name = Name
        self.Description = Description
        self.CreateDate = CreateDate


if __name__ == '__main__':
    manager.run()
