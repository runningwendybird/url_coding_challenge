from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import jinja2
import json
import parse_html

app = Flask(__name__)
app.secret_key = "TESTINGKEY"
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def landing_page():
	return render_template("home.html")

@app.route("/results")
def get_results():
	results = parse_html.return_links("http://runfreerunme.herokuapp.com")
	json_results = json.dumps(results)
	return json_results
