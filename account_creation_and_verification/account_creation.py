from flask import Flask, request, render_template, flash, redirect, url_for, Blueprint
from password_handler import password_checker
from sql_commands import insert_username_and_password, check_for_username, check_password

account_creation_verification = Flask(__name__, template_folder='../templates')
creating_verifying_account = Blueprint('creating_verifying_account', __name__, static_folder='../static', template_folder='../templates')
account_creation_verification.secret_key= "Isai_secret_key"

@account_creation_verification.route('/login', methods = ["POST", "GET"])
def create():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        username_validity = check_for_username(username)
        password_validity = password_checker(password)
        if username_validity and password_validity:
            insert_username_and_password(username, password)
            flash('Account Creation Successful!', 'info')
            flash('Please Login with Your account Information', 'info')
            return redirect(url_for("verify"))
        elif username_validity and not password_validity:
            flash('Password did not meet qualifications', 'info')
            return redirect(url_for("create"))
        elif not username_validity and password_validity:
            flash('Username Already in Use', 'info')
            return redirect(url_for("create"))
        elif not username_validity and not password_validity:
            flash('Username Already in Use and Password did not meet qualifications', 'info')
            return redirect(url_for("create"))
    else:
        return render_template("templates_for_creating_and_logging_in/account_creation.html")


@account_creation_verification.route('/', methods = ["POST", "GET"])
def verify():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        username_validity = check_for_username(username)
        if username_validity:
            password_validity = check_password(username, password)
            if password_validity:
                flash('Login Successful', 'info')
                return render_template('homepage.html')
            else:
                flash('Password is incorrect', 'info')
                return redirect(url_for("verify"))
        else:
            flash("Username doesn't exist", 'info')
            return redirect(url_for("verify"))
    else:
        return render_template("templates_for_creating_and_logging_in/account_verification.html")

if __name__ == '__main__':
    account_creation_verification.run(debug=True)



