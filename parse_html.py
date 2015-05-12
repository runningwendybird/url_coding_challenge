import urllib2
import re
import urlparse

def return_links(my_url):
	"""Opens url, reads it, finds the links using 
	regular expressions and returns them."""
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

	domain = "/" + domain
	return domain



