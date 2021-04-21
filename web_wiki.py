import urllib2
response = urllib2.urlopen('https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=goetsch&format=json')
html = response.read()
print(html)
