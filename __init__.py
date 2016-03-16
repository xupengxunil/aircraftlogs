from flask import Flask, render_template, flash, request, url_for, redirect, session
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc

from forms import RegistrationForm
from content_management import Content
from dbconnect import connection

TOPIC_DICT = Content()

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/dashboard/')
def dashboard():
    # flash('Welcome user')
    return render_template("dashboard.html")


@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        attempted_username = request.form['username']
        attempted_password = request.form['password']

        if attempted_username == "admin" and attempted_password == "admin":
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid credentials. Try again."
            flash(error)
    return render_template("login.html")


@app.route('/register/', methods=['GET', 'POST'])
def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)",
                          (thwart(username)))
            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('register.html', form=form)

            else:
                c.execute("INSERT INTO users (username, password, email) VALUES (%s) (%s) (%s)",
                          (thwart(username), thwart(password), thwart(email)))
                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('dashboard'))

        return render_template('register.html', form=form)

    except Exception as e:
        return str(e)
        # return render_template("errors/500.html", error=e)


if __name__ == '__main__':
    app.run()


"""
Helpful debugging code for new page
@app.rout('/example')
def example():
    try:
        return render_template("example.html", VARIABLE_TO_BE_PASSED = VARIABLE)
    except Exception as e:
        return render_template("500.html", error = e)
"""
