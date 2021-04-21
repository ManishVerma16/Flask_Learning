from market import app
from flask import render_template
from market.models import Item


@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/market')
def marketPage():
    items = Item.query.all()
    return render_template('market.html', items=items)