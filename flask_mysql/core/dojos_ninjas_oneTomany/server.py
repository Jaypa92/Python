from flask import Flask, render_template, request, redirect
from dojo import Dojo
from ninja import Ninja

app = Flask(__name__)

@app.route("/")
def index():

    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojo_index.html",dojos = dojos)

@app.route("/ninjas")
def ninjas():

    dojos = Dojo.get_all()

    return render_template("ninja.html",dojos = dojos)


@app.route("/create_dojo", methods=["POST"])
def create_dojo():

    data = {
        "name": request.form["name"],

    }

    Dojo.save(data)

    return redirect("/")

@app.route("/create_ninja",methods=["POST"])
def create_ninja():

    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }

    Ninja.save(data)

    return redirect("/ninjas")

@app.route("/dojo_members/<int:id>")
def display_ninjas(id):

    data = {
        "id" : id
        }

    dojo = Dojo.get_dojos_with_ninjas(data)
    print(ninjas)
    return render_template('ninja_list.html',dojo= dojo)
            
if __name__ == "__main__":
    app.run(debug=True)
