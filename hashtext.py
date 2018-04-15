from hashing import hashtext
text = str(input("please your text >"))
while text == '':
    print("please your text !!")
    text = str (input("please your text >"))
hashtype = str(input("please hashtype >"))

while hashtype == '':
    print ("please your hashtype !!")
    hashtype = str(input("please your hashtype >"))
h = hashtext()
print (h.hashingtext(text,hashtype))
