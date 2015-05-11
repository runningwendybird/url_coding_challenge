import urllib2

def return_links(my_url):
	f = urllib2.urlopen(my_url)
	links = []
	link_indicator = "href"
	for line in f:
		split_line = line.split()
		for element in split_line:
			if link_indicator in element:
				links.append(element)

	return links
