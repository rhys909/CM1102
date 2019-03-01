from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2be252e90be41fdf9140c33eee20a86a8cee3c07a997fe1c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1821631:H0tr0d99@csmysql.cs.cf.ac.uk:3306/c1821631'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from shop import routes
