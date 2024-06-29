from flask import Flask, render_template
server = Flask(__name__)
@server.route("/play")
def show_html():
    return render_template("index.html",num=3)
@server.route("/play/<int:num>")
def more_box(num):
    return render_template("index.html",num = num)
@server.route("/play/<int:num>/<string:color>")
def add_more(num, color):
    return render_template("index.html",num = num, color= color)

if __name__ == "__main__":
    server.run(debug = True)