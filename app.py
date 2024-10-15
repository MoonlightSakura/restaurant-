from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/restaurant"
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_menu_item', methods=['GET', 'POST'])
def add_menu_item():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        mongo.db.menu.insert_one({'name': name, 'price': float(price), 'description': description})
        return redirect(url_for('home'))
    return render_template('add_menu_item.html')

@app.route('/add_reservation', methods=['GET', 'POST'])
def add_reservation():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        guests = request.form['guests']
        mongo.db.reservations.insert_one({
            'name': name,
            'date': date,
            'time': time,
            'guests': int(guests)
        })
        return redirect(url_for('home'))
    return render_template('add_reservation.html')

@app.route('/bookings')
def bookings():
    reservations = mongo.db.reservations.find()
    return render_template('bookings.html', reservations=reservations)

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change the port here if needed
