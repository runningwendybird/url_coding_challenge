import urllib2
import re


def return_links(my_url):
	s = urllib2.urlopen(my_url)
	s = s.read()
	urls = re.findall(r'href=[\'"]?([^\'" >]+)', s)
	return urls



