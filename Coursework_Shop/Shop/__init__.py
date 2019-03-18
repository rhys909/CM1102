from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_folder="Static")
app.config['SECRET_KEY'] = 'dd8382eff8d9254f376806101a3e7bebd68b0b21a80178b0'
#app.config['WTF_CSRF_SECRET_KEY']='e9ee2c5930d1a90072fdb21464b64145e5f0d6a0afb4fcd6'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://c1821631:H0tr0d99@csmysql.cs.cf.ac.uk:3306/c1821631'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from Shop import routes
