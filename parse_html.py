import urllib2

def print_html(my_url):
	f = urllib2.urlopen(my_url)
	print f.read()