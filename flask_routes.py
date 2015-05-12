from flask import Flask, request, render_template
import jinja2
import parse_html # a module I wrote 
import os
from flask.ext.cache import Cache
from datetime import datetime

app = Flask(__name__)
app.secret_key = "TESTINGKEY"
app.jinja_env.undefined = jinja2.StrictUndefined
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/")
def landing_page():
	"""Renders the home page template"""
	return render_template("home.html")

@app.route("/results")
def get_results():
	"""Finds the appropriate links and renders the results page."""
	my_url = request.args.get("url")
	results = get_results(my_url)
	return render_template("results.html", results = results[0], domain = results[1], url = my_url, time = results[2])



@cache.memoize(timeout=1800)
def get_results(my_url):
	"""Determines the domain, the links for that domain, and gives a time stamp. Results are cached."""
	links = parse_html.return_links(my_url)
	domain = parse_html.determine_domain(my_url)
	sorted_links = []
	for link in links:
		if domain in link:
			sorted_links.append(link)
	time = datetime.now()
	results = (sorted_links, domain, time)
	return results

