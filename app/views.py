from flask import render_template, flash, request, url_for, redirect, session
from passlib.hash import sha256_crypt
import gc

from app import app
from app.models import RegistrationForm, LoginForm


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


@app.route('/', methods=['GET', 'POST'])
def homepage():
    error = None
    form = LoginForm(request.form)

    return render_template("main.html", form=form, error=error)


@app.route('/dashboard/')
def dashboard():
    # flash('Welcome user')
    return render_template("dashboard.html")


@app.route('/register/', methods=['GET', 'POST'])
def register_page():

    form = RegistrationForm(request.form)

    # if request.method == "POST" and form.validate():
    #     username = form.username.data
    #     email = form.email.data
    #     password = sha256_crypt.encrypt((str(form.password.data)))
    #     c, conn = connection()
    #
    #     sql_check_reg = "SELECT * FROM users WHERE username = (%s)"
    #     x = c.execute(sql_check_reg, (username,))
    #
    #     if int(x) > 0:
    #         flash("That username is already taken, please choose another")
    #         return render_template('register.html', form=form)
    #
    #     else:
    #         sql_insert_reg = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
    #         c.execute(sql_insert_reg, (username, password, email))
    #         conn.commit()
    #         flash("Thanks for registering!")
    #         c.close()
    #         conn.close()
    #         gc.collect()
    #
    #         session['logged_in'] = True
    #         session['username'] = username
    #
    #         return redirect(url_for('dashboard'))

    return render_template('register.html', form=form)


@app.route('/login/', methods=["GET", "POST"])
def login_page():
    error = None

    form = LoginForm(request.form)

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
    return render_template('login.html', form=form, error=error)


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