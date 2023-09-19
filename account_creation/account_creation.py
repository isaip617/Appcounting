from flask import Flask, request, render_template, flash
from password_handler import password_checker
from sql_commands import insert_username_and_password, check_for_username

account_creation = Flask(__name__)

@account_creation.route('/', methods = ["POST", "GET"]):
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if check_for_username(username) and password_checker(password):
            insert_username_and_password(username, password)
            return render_template('Homepage.html')
        elif check_for_username(username) and not password_checker(password):
            flash('Password did not meet qualifications')
        elif not check_for_username(username) and password_checker(password):
            flash('Username Already in Use')
        elif not check_for_username(username) and not password_checker(password):
            flash('Username Already in Use and Password did not meet qualifications')
    else:
        return render_template("account_creation.hmtl")




