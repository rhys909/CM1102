from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET KEY'] = 'dd8382eff8d9254f376806101a3e7bebd68b0b21a80178b0'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://c1821631:H0tr0d99@csmysql.cs.cf.ac.uk:3306/c1821631'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from Shop import routes
