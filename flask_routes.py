from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import jinja2
import json

app = Flask(__name__)
app.secret_key = "TESTINGKEY"
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def landing_page():
	return render_template("home.html")

@app.route("/results")
def get_results():
	results = ["this is my result."]
	json_results = json.dumps(results)
	return json_results
