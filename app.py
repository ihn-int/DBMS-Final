from flask import Flask, render_template, request, redirect, url_for
import json

accounts = [1234567, 23456789]


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/sign")
def sign():
    return render_template("sign.html")

@app.route("/success")
def success():
    return "SUCCESS"

@app.route("/regist", methods = ["POST"])
def regist():
    form = request.form
    
    #account = form.getkeys("account")
    #passed = form.getkeys("password")
    for i, m in form.iteritems():
        print(i, m)
    #print(form, account, passed)

    return redirect(url_for("success"))

if __name__ == "__main__":
    app.run()
