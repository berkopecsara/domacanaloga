from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/marriage/"
html = urlopen(url).read()

prva_stran = BeautifulSoup(html)
print(prva_stran.html.head.title.string)

porocni_citati = prva_stran.findAll("p", {"class": "quoteContent"})
for s in porocni_citati:
    if "marriage" in s.string:
        print s.string

print ("I LOVE YA")
