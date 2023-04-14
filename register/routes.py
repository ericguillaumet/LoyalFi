from flask import render_template
from register import app

@app.route("/", methods=("GET", "POST"))

def index():
    return render_template("index.html",pageTitle="LoyalFi")

@app.route("/claim",methods=["GET","POST"])

def claim():
    return render_template("claim.html", pageTitle="Claim")

@app.route("/ranking", methods=["GET"])
def ranking():
    return render_template("ranking.html", pageTitle="Ranking")