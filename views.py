import sqlite3
from functools import wraps
from flask import Flask, render_template, request, session, g, flash, url_for, redirect
from twilio.rest import TwilioRestClient

app = Flask(__name__)
app.config.from_object('_config')

# user_info(phone_number TEXT, zipcode TEXT, verified INT, subscribed INT)
def connect_db():
    """change this later so that we only need a one-liner to connect to
    the user_info table and get a curosr object""" 
    return sqlite3.connect(app.config['DATABASE'])


def send_text_message(user_phone_number, message):
    client = TwilioRestClient(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])
    client.messages.create(to=user_phone_number, from_="+18024488492", body=message)

def make_sure_user_doesnt_already_exist():
    """connect to the database and make sure the phone number entered isn't already there.
    This function should be called by signup()
    """
    pass


##################################################################################
##### Need to validate the phone number and zip code on the front end ############
##################################################################################


def send_test_message_to_new_user(phone_number):
    """send test text message to user. only add user to DB if verified."""
    send_text_message(user_phone_number, "Hey, are you there?")


def grab_new_user_response():
    """receives response from new user and maybe eventually
    parses it out for different actions."""
    pass


def stop_spamming_me():
    """unsubscribes user, without removing them from DB
    we need to add a new DB column for this
    """
    pass


@app.route('/')
def home():
    """collects phone number and zipcode, and pushes it into the database."""
    return render_template('home.html')


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    zipcode = request.form['zipcode']
    phone_number = request.form['phone_number']
    if not zipcode or not phone_number:
        flash("Please fill out all fields.")
        return redirect(url_for('add_user'))
    with connect_db() as connection:
        c = connection.cursor()
        c.execute("INSERT INTO user_info VALUES(?,?,?,?)", [phone_number, zipcode, 0, 0])
    send_text_message(phone_number, "Greetings from RainMan.io! To subscribe and receive weather updates from us, text any message back and you'll be good to go, dude.")
    flash("Thanks for signing up! You will receive a text message with instructions to subscribe and customize your RainMain.io experience!")
    return redirect(url_for('home'))
