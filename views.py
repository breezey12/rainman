import sqlite3
from functools import wraps
from flask import Flask, render_template, request, session, g, flash, url_for, redirect

app = Flask(__name__)
app.config.from_object('_config')

# user_info(username TEXT, password TEXT, zipcode INT, phone_number TEXT) 
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def make_sure_user_doesnt_already_exist():
    pass


def validate_phone_num():
    pass


def validate_zipcode():
    pass


def verify_sms_ownership():
    pass


def stop_spamming_me():
    """unsubscribes user, without removing them from DB
    we need to add a new DB column for this
    """
    pass

@app.route('/', methods=['GET', 'POST'])
def home():
   """logs user into dashboard"""
   return render_template('home.html')


@app.route('/signup')
def signup():
    """collects username, password, zipcode and phone number
    and pushes it into the database"""
    return render_template('signup.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    zipcode = request.form['zipcode']
    phone_number = request.form['phone_number']
    if not zipcode or not phone_number:
        flash("Please fill out all fields")
        return redirect(url_for('signup'))
    with connect_db() as connection:
        c = connection.cursor()
        c.execute("INSERT INTO user_info VALUES(?,?,?,?)", [username, password, zipcode, phone_number])
    confirmation_message = "Okay, cool!  You're gonna get weather updates on your phone, dude."
    return redirect(url_for('home'))
