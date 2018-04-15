from bs4 import BeautifulSoup
import urllib.request
url = "https://www.google.com"
openurl = urllib.request.urlopen(url)
html_content = str(openurl.read(12000))
soup = BeautifulSoup(html_content , 'html.parser')
print (soup.prettify())
