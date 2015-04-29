import sqlite3
from functools import wraps
from flask import Flask, render_template, request, session, g, flash, url_for, redirect

app = Flask(__name__)
app.config.from_object('_config')

# user_info(username TEXT, password TEXT, zipcode INT, phone_number TEXT) 
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def make_sure_user_doesnt_already_exist():
    """connect to the database and make sure the phone number entered 
    isn't already in there.
    This function should be called by signup()
    """
    pass

##################################################################
##### we need to validate the phone number and zip code on the front end #####



def send_test_message_to_new_user():
    """send test text message to user. only add user to DB if verified."""
    pass


def grab_new_user_response():
    """receives response from new user and maybe eventually
    parses it out for different actions."""


def stop_spamming_me():
    """unsubscribes user, without removing them from DB
    we need to add a new DB column for this
    """
    pass


@app.route('/')
def home():
    """collects username, password, zipcode and phone number
    and pushes it into the database"""
    return render_template('home.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    zipcode = request.form['zipcode']
    phone_number = request.form['phone_number']
    if not zipcode or not phone_number:
        flash("Please fill out all fields")
        return redirect(url_for('signup'))
    with connect_db() as connection:
        c = connection.cursor()
        c.execute("INSERT INTO user_info VALUES(?,?,?,?)", [phone_number, zipcode, 0, 0])
    confirmation_message = "Okay, cool!  You're gonna get weather updates on your phone, dude."
    return redirect(url_for('home'))
