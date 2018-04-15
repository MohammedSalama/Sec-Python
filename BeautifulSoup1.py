from bs4 import BeautifulSoup
import urllib.request
url = "http://nurseslabs.com"
openurl = urllib.request.urlopen(url)
html_content = str(openurl.read(10240))
soup = BeautifulSoup(html_content , 'html.parser')
#print (soup.html.head.title)
#print (soup.html.head.title.text)
#print (soup.find("p"))
#print (soup.prettify())
#print (soup.find("link"))
#print (soup.findAll("p"))
for i in soup.findAll("link"):
    print (i)
    #print (i.get("href"))
