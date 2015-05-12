from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import jinja2
import json
import parse_html
import urllib
import urlparse
import os

app = Flask(__name__)
app.secret_key = "TESTINGKEY"
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def landing_page():
	return render_template("home.html")

@app.route("/results")
def get_results():
	my_url = request.args.get("url")
	results = parse_html.return_links(my_url)
	domain = parse_html.determine_domain(my_url)
	sorted_results = []
	for result in results:
		if domain in result:
			sorted_results.append(result)
	return render_template("results.html", results = sorted_results, domain = domain, url = my_url)

