import urllib2
import re
import urlparse

def return_links(my_url):
	s = urllib2.urlopen(my_url)
	s = s.read()
	urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)
	return urls

def determine_domain(my_url):
	hostname = urlparse.urlparse(my_url)[1]
	return hostname



