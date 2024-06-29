from flask import Flask, render_template,session
app = Flask(__name__)
app.secret_key = "blah blah blah"

@app.route("/")
def index():
    return render_template("checkerboard_index.html", x=8, y=8)

@app.route("/<int:x>")
def x_size(x):
    return render_template("checkerboard_index.html", x = x, y=8)

@app.route("/<int:x>/<int:y>")
def x_plus_y(x,y):
    return render_template("checkerboard_index.html",x=x,y=y)

@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def adds_colors(x,y,color1,color2):
    return render_template("checkerboard_index.html", x=x,y=y,color1=color1,color2=color2)
if __name__ == "__main__":
    app.run(debug=True)