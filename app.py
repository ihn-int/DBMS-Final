from flask import Flask, render_template, request, redirect, url_for
import json
import hashlib
import db
users = {
    "12345678" : "25d55ad283aa400af464c76d713c07ad",
    "13572468" : "7a386acb9e2b1d09512b5e74934acdff",
}

app = Flask(__name__)
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/sign")
def sign():
    return render_template("sign.html")

@app.route("/success")
def success():
    return "SUCCESS"

@app.route("/failed")
def failed():
    return "FAILED"

@app.route("/unknown")
def unknown():
    return "UNKNOWN"

@app.route("/regist", methods = ["POST"])
def regist():
    account = request.form["account"]
    passwd = request.form["password"]
    if account in users:
        
        hash = hashlib.md5(passwd.encode("utf-8")).hexdigest()
        if users[account] == hash:
            return redirect(url_for("success"))
        else:
            print(hash)
            return redirect(url_for("failed"))
    else:
        return redirect(url_for("unknown"))

if __name__ == "__main__":
    app.run(debug = True, host = "140.113.89.236", port = 5000)
