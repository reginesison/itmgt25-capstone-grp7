from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "itm_is_fun<333"

@app.route("/stock", methods=['POST', 'GET'])
def index():
    flash("What is the stock market value in this country?")
    return render_template("index.html")

@app.route("/show", methods=['POST', 'GET'])
def show():
    flash("This is the stock market value in " + str(request.form["name_input"]))
    return render_template("index.html")