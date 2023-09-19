from flask import Flask, request, render_template, flash, redirect, url_for
from password_handler import password_checker
from sql_commands import insert_username_and_password, check_for_username

account_creation = Flask(__name__, template_folder='../templates')
account_creation.secret_key= "Isai_secret_key"

@account_creation.route('/hello', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        username_validity = check_for_username(username)
        password_validity = password_checker(password)
        if username_validity and password_validity:
            insert_username_and_password(username, password)
            return render_template('Homepage.html')
        elif username_validity and not password_validity:
            flash('Password did not meet qualifications', 'info')
            return redirect(url_for("login"))
        elif not username_validity and password_validity:
            flash('Username Already in Use', 'info')
            return redirect(url_for("login"))
        elif not username_validity and not password_validity:
            flash('Username Already in Use and Password did not meet qualifications', 'info')
            return redirect(url_for("login"))
    else:
        return render_template("account_creation.html")

if __name__ == '__main__':
    account_creation.run(debug=True)




