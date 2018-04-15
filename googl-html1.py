from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
from urllib.request import Request
search = str(input("<Search > "))
searchp = {"q":"{0}".format(search)}
searchpencode = urllib.parse.urlencode(searchp)
url = Request("https://pipl.com/search/" + "?" + searchpencode + "&l=&sloc=&in=6",headers={'User-Agent':'Mozilla/5.0'})
openurl = urllib.request.urlopen(url)
content = str(openurl.read(50000))
#print(content)
soup = BeautifulSoup(content , "html.parser")
for i in soup.findAll("div",{"class":"title truncate"}):
    print (i.a.text.rstrip("\n"))
    print ("https://pipl.com/"+i.a.get("href").rstrip("\n"))
    
