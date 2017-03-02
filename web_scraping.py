from urllib2 import urlopen
from bs4 import BeautifulSoup

url = "https://scrapebook22.appspot.com/"
html = urlopen(url).read()

prva_stran = BeautifulSoup(html)
print(prva_stran.html.head.title.string)

for povezava in prva_stran.findAll("a"):
    if povezava.string == "See full profile":
        url_profila = url + povezava["href"]
        html_profila = urlopen(url_profila).read()

        profil = BeautifulSoup(html_profila)
        email_span = profil.find("span", {"class": "email"})
        print(email_span.string)

        vsi_spani = profil.findAll("span")
        for s in vsi_spani:
            #print(s)
            if s.has_key("data-city"):
                print(s.string)
                break
        print("------")