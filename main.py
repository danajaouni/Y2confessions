from flask import Flask, render_template, request,redirect, url_for
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

@app.route("/" , methods = ['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")
  else:
    form = request.form
    message = request.form['message']
    hub = request.form['hub']
    add_Confession(message, hub)
    if request.method == 'POST':
      return redirect(url_for('confessions'))


@app.route('/confessions')
def confessions():
  return render_template('confessions.html', confessions=session.query(Confession).all())


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
