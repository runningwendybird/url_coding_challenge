from bs4 import BeautifulSoup
import urllib2
from tld import get_tld

def return_links(my_url):
	"""Opens url, reads it, finds the links using 
	regular expressions and returns them. Links are not sorted."""
	s = urllib2.urlopen(my_url)
	s = s.read()
	soup = BeautifulSoup(s)
	urls = []
	for link in soup.find_all('a'):
		urls.append(link.get('href'))
	return urls

def determine_domain(my_url):
	"""Returns the domain for a given url."""
	domain = get_tld(my_url)
	return domain


# tests to run with pytest

def test_links():
	assert return_links("http://twinoaksgrowers.com") == ["/products.htm", "/avail/", "/care.htm", 
	"/news.htm", "/contact.htm"] 

def test_domain():
	assert determine_domain("http://www.twitter.com") == "twitter.com"

def test_links_more_difficult():
	assert return_links("http://runfreerunme.herokuapp.com") == ["/", "/about", "/business", "/about", 
	"/business", "http://www.github.com/runningwendybird/runfree", "/demo", "http://www.github.com/runningwendybird",
	"http://www.twitter.com/runwendybird", "https://www.linkedin.com/in/hayleydenbraverpe", 
	"mailto:hayley.denbraver@gmail.com", "/about", "/new_user", "www.hackbrightacademy.com", 
	"http://www.github.com/runningwendybird", "http://www.twitter.com/runwendybird", 
	"https://www.linkedin.com/in/hayleydenbraverpe", "mailto:hayley.denbraver@gmail.com"]