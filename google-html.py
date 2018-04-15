from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
searchp = {"s":"heart coma"}
searchpencode = urllib.parse.urlencode(searchp)
url = "http://nurseslabs.com/"
url = url + "?" + searchpencode
openurl = urllib.request.urlopen(url)
htmlcon = openurl.read(500000)
soup = BeautifulSoup(htmlcon , "html.parser")
for i in soup.findAll("h3",{"class" : "entry-title td-module-title"}):
     print (i.a.text)
