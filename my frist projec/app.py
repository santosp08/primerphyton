from flask import Flask, render_template

var_app = Flask(__name__)

@var_app.route("/")
def inicio():
    return "hola mundo"


@var_app.route("/cur")
def cur():
    return render_template('frontend/cur.html')

if __name__== "__main__":
    var_app.run(debug=True,port=3000)