from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route("/")
def index():
    user = User.get_all()

    return render_template("Read.html",user=user)

@app.route("/create")
def create():
    return render_template("Create.html")

@app.route('/create_user', methods=["POST"])
def create_user():

    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }

    User.save(data)
    
    return redirect('/')