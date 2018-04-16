import urllib.request
from tqdm import tqdm
from optparse import OptionParser
parse = OptionParser("""
script.py [option]
===================================>
-u / --url :: link
-d / --dir :: dir
ex:
script.py -u http://www.kau.edu.sa/Files/830/Files/60671_Linux.pdf
script.py --url http://www.kau.edu.sa/Files/830/Files/60671_Linux.pdf
script.py -d C:/Users/Muhammed Salama/Desktop/
script.py --dir  C:/Users/Muhammed Salama/Desktop/
""")
parse.add_option("-u","--url",dest="url",type="string",help="url please")
parse.add_option("-d","--dir",dest="dir",type="string",help="dir please")
(options , args) = parse.parse_args()
if options.url == None:
    print(parse.usage)
    exit(0)
else:
    url = str(options.url)
    if options.dir != None:
        D = str(options.dir)
        file_name = url.split("/")[-1]
        opfile = open(D+""+file_name,"wb")
    else:
        opfile = open(file_name,"wb")
    opurl = urllib.request.urlopen(url)
    print(opurl.info())
    block_sz = 590
    file_size = int(opurl.headers["Content-Length"])
    for i in tqdm(range(file_size)):
        buffer = opurl.read(block_sz)
        i = i + block_sz
        opfile.write(buffer)
    opfile.close()
