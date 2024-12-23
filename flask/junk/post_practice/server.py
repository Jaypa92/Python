from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "whatever"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    
    session['username'] =request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route("/show")
def show_user():
    return render_template("index_2.html")

if __name__ == "__main__":
    app.run(debug=True)
