from Shop import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    part = db.relationship('Part', backref='manufacturer', lazy=True)

    def __repr__(self):
        return f"Manufacturer('{self.name}')"

class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70),nullable=False)
    category = db.Column(db.String(15), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='No_Image.png')
    stock_level = db.Column(db.Integer, nullable=False)
    Manufacturer_ID = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)

    def __repr__(self):
        return f"Part('{self.name}', '{self.description}', '{self.price}', '{self.stock_level}', '{self.category}')"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

#If you want your cart to be stored in db, specify a model for it here, e.g.
# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer)
#     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
#     etc. ....
