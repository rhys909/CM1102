import os
from flask import render_template, url_for, request, redirect, flash
from shop import app, db
from shop.models import Manufacturer, Items, User
from shop.form import sign_up_form, login_form
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', Items = items, title='PC Store - Home')
@app.route("/about")
def about():
    return render_template('about.html', title='PC Store - About')
@app.route("/item_page")
def item_page():
    return render_template('item_page.html', title='PC Store - Items')
@app.route()
@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    form = sign_up_form
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('sign_up.html', title='PC Store - Sign Up', form=form)
@app.route("/login", methods=['GET', 'POST'])
def login():
    form= login_form()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password!")
            return redirect(url_for('login'))
    return render_template('login.html', title='PC Store - Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/add_to_basket/<int:item_id>")
def add_to_basket(item_id):
    if "basket" not in session:
        session["basket"] = []
    session["basket"].append(item_id)
    flash("The item has been added to your shopping basket!")
    return redirect("/basket")
@app.route("/basket", methods=['GET', 'POST'])
def basket_display():
    if "cart" not in session:
        flash('There is nothing in your basket!')
        return render_template("basket.html")
    else:
        items = session["basket"]
        cart = {}

        total_price = 0
        total_quantity = 0
        for item in items:
            part = Items.query.get_or_404(item)
            total_price += part.price
            if part.id in cart:
                basket[part.id]["quantity"] += 1
            else:
                basket[part.id] = {"quantity":1, "title": part.title, "price": part.price}
            total_quantity = sum(item["quantity"] for item in basket.values())

        return render_template("basket.html", title='Your Shopping Cart', display_basket = basket, total = total_price, total_quantity = total_quantity)
    return render_template("basket.html")
