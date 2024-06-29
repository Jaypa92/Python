from flask import Flask, render_template, redirect, session, request
import random
app =  Flask(__name__)
app.secret_key = "coolnow"

@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 0
    if "count" in session:
        session["count"] += 1
    if "num" not in session:
        session["num"] = random.randint(1, 100)
        print("num")
    return render_template("counter_game_index.html")

@app.route("/process", methods=["POST"])
def process():
    session["guess"] = int(request.form["guess"])
    return redirect("/")

@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
