import urllib2
import re
import urlparse

def return_links(my_url):
	"""Opens url, reads it, finds the links using 
	regular expressions and returns them. Links are not sorted."""
	s = urllib2.urlopen(my_url)
	s = s.read()
	urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)
	return urls

def determine_domain(my_url):
	"""Returns the domain for a given url."""
	domain = urlparse.urlparse(my_url)[1]
	# checks to see if 'www.' is in front of domain.
	# if so removes it from the domain.
	if domain[:4] == "www.":
		domain = domain[4:]

	return domain

def test_links():
	assert return_links("http://twinoaksgrowers.com") == ["/format/standard.css", "/format/print.css", "/products.htm", "/avail/", "/care.htm", "/news.htm", "/contact.htm"] 

def test_domain():
	assert determine_domain("http://www.twitter.com") == "twitter.com"

def test_links_more_difficult():
	assert return_links("http://runfreerunme.herokuapp.com") == ["/static/bootstrap/css/bootstrap.min.css", "http://fonts.googleapis.com/css?family=Quando", "/static/winged.ico", "/", "/about", "/business", "/about", "/business", "http://www.github.com/runningwendybird/runfree", "/demo", "http://www.github.com/runningwendybird", "http://www.twitter.com/runwendybird", "https://www.linkedin.com/in/hayleydenbraverpe", "mailto:hayley.denbraver@gmail.com", "/about", "/new_user", "www.hackbrightacademy.com", "http://www.github.com/runningwendybird", "http://www.twitter.com/runwendybird", "https://www.linkedin.com/in/hayleydenbraverpe", "mailto:hayley.denbraver@gmail.com"]