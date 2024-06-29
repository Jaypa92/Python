from flask import Flask, render_template,session,redirect,request
app = Flask(__name__)
app.secret_key = "blahblahblah"

@app.route("/")
def index():
    return render_template("dojo_survey_index.html")
@app.route("/process", methods=["POST"])
def accept():
    session["name"] = request.form["name"]
    session["place"] = request.form["place"]
    session["lang"] = request.form["language"]
    session["user-comments"] = request.form["comments"]
    return redirect("/result")
@app.route("/result")
def result():

    return render_template("dojo_survey_index_2.html")

if __name__=="__main__":
    app.run(debug=True)