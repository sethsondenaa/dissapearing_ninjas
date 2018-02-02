from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/ninjas")
def tmnt():
	return render_template("ninjas.html")

@app.route("/ninjas/<color>")
def ninjas(color):
	if color == "blue":
		return render_template("leonardo.html")
	elif color == "orange":
		return render_template("michelangelo.html")
	elif color == "red":
		return render_template("raphael.html")
	elif color == "purple":
		return render_template("donatello.html")
	else:
		return render_template("notApril.html")

app.run(debug=True)