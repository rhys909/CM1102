import os
from flask import render_template, url_for, request, redirect, flash, session, jsonify
from Shop import app, db
from Shop.models import Manufacturer, Part, User
from Shop.form import sign_up_form, login_form
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")

@app.route("/home" methods=['GET', 'POST'])
def home():
    parts = Part.query.all()
    form = sort_items()
    return render_template('home.html', parts=parts, form=form, title='PC Store - Home')

@app.route("/about")
def about():
    return render_template('about.html', title='PC Store - About')

@app.route("/part/<int:part_id>")
def part(part_id):
    part = Part.query.get_or_404(part_id)
    return render_template('part.html', part=part, title='PC Store Item')

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    form = sign_up_form()
    if form.validate_on_submit():
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
            flash("Login successful!!")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password!")
            return redirect(url_for('login'))
    return render_template('login.html', title='PC Store - Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/add_to_basket/<int:part_id>")
def add_to_basket(part_id):
    if "basket" not in session:
        session["basket"] = []

    session["basket"].append(part_id)

    flash("The item has been added to your shopping basket!")
    return redirect("/basket")

@app.route("/basket", methods=['GET', 'POST'])
def basket_display():
    if "basket" not in session:
        flash('There is nothing in your basket!')
        return render_template("basket.html", display_basket = {}, total = 0)
    else:
        items = session["basket"]
        basket = {}

        total_price = 0
        total_quantity = 0
        for item in items:
            part = Part.query.get_or_404(item)

            total_price += part.price
            if part.id in basket:
                basket[part.id]["quantity"] += 1
            else:
                basket[part.id] = {"quantity":1, "name": part.name, "price": part.price}
            total_quantity = sum(item["quantity"] for item in basket.values())

        return render_template("basket.html", title='Your Shopping Basket', display_basket = basket, total = total_price, total_quantity = total_quantity)
    return render_template("basket.html")

@app.route("/delete_item/<int:item_id>", methods=['GET', 'POST'])
def delete_item(item_id):
    if "basket" not in session:
        session["basket"]=[]
    session["basket"].remove(item_id)
    flash("You have removed an item from your basket!")
    session.modified = True
    return redirect("/basket")

#@app.route("/checkout")
#def checkout():
