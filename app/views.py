from flask import (render_template, flash, request,
                   url_for, redirect, session, g)
from functools import wraps
from passlib.hash import sha256_crypt
import gc

from app.models import User

from app import app, db
from app.forms import RegistrationForm, LoginForm


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Must be logged in")
            return redirect(url_for('homepage'))
    return wrap


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@app.route('/', methods=['GET', 'POST'])
def homepage():
    error = None
    login_form = LoginForm(request.form)
    reg_form = RegistrationForm(request.form)

    return render_template("main.html",
                           login_form=login_form,
                           reg_form=reg_form,
                           error=error)


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route('/register/', methods=['GET', 'POST'])
def register_page():
    reg_form = RegistrationForm(request.form)

    if request.method == "POST":
        if reg_form.validate() is False:
            return render_template('register.html',
                                   reg_form=reg_form)
        else:
            new_user = User(
                reg_form.first_name.data,
                reg_form.last_name.data,
                reg_form.username.data,
                reg_form.email.data,
                reg_form.password.data
            )
            db.session.add(new_user)
            db.session.commit()
            gc.collect()
            session['logged_in'] = True
            session['username'] = new_user.username
            flash('Thank you for registering!')
            return redirect(url_for('dashboard'))

    elif request.method == "GET":
        return render_template('register.html',
                               reg_form=reg_form)


@app.route('/login/', methods=["GET", "POST"])
def login_page():
    error = None
    login_form = LoginForm(request.form)

    # if request.method == "POST":
    #     c, conn = connection()
    #     username = form.username.data
    #     sql_query = "SELECT * FROM users WHERE username = (%s)"
    #     data = c.execute(sql_query, (username,))
    #     data = c.fetchone()[2]
    #
    #     if sha256_crypt.verify(form.password.data, data):
    #         session['logged_in'] = True
    #         session['username'] = username
    #         flash('Hello %s.' % username)
    #         gc.collect()
    #         return redirect(url_for('dashboard'))
    #
    #     else:
    #         error = "Invalid credentials, try again."
    #
    # gc.collect()
    return render_template('login.html',
                           login_form=login_form,
                           error=error)


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    flash("You have been logged out.")
    gc.collect()
    return redirect(url_for('homepage'))


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