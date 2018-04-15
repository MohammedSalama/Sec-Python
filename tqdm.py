import urllib.request
url = "http://www.kau.edu.sa/Files/830/Files/60761_Linux.pdf"
opurl = urllib.request.urlopen(url)
print (opurl.info())
file_name = url.split("/")[-1]
opfile = open(file_name,"wb")
opfile.write(opurl.read())
opfile.close()
