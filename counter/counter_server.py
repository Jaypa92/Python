from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Whatever"

@app.route("/")
def index():
    if "num" not in session:
        session["num"] = 0
        
    return render_template("counter_index.html")
@app.route("/counter")
def counter():
    session["num"]+=1
    return redirect("/")
@app.route("/destroy_session")
def destroy():
    session.clear()

    return redirect ("/")
        


if __name__ == "__main__":
    app.run(debug=True)