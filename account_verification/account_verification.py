from flask import Flask, request, render_template, flash, redirect, url_for, Blueprint
from sql_commands import check_password, check_for_username

account_verification = Flask(__name__, template_folder='../templates')
verifying_account = Blueprint('verifying_account', __name__, static_folder='../static', template_folder='../templates')
account_verification.secret_key= "Isai_secret_key"

@account_verification.route('/', methods = ["POST", "GET"])
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
    account_verification.run(debug=True)




