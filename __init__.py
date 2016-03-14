from flask import Flask, render_template, flash

from content_management import Content

TOPIC_DICT = Content()

app = Flask(__name__) 

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    flash('Welcome user')
    return render_template("dashboard.html")

@app.route('/log/', methods=['GET', 'POST'])
def log():
    return render_template("log.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html")

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