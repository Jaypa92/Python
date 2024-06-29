from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html", banana = "Shoot", num = 3)
@app.route("/dojo")
def dojo():
    return "Dojo!"
@app.route("/say/<string:name>")
def hello_person(name):
    return '"' + f'Hi {name.capitalize()}!' + '"'
@app.route("/repeat/<int:num>/<string:name>")
def repeating(num, name):
    return name * num
@app.errorhandler(404)
def error(e):
    return "Sorry! No response. Try again"
if __name__ == "__main__":
    app.run(debug=True)