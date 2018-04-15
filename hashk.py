from hashing import hashtext
from readhw import Readw
the_hash = str(input("the hash: "))
the_wordlist = str(input("the wordlist: "))
the_hash_type = str(input("the hash_type: "))
RR = Readw()
readall = RR.Readwlist(the_wordlist)
HH = hashtext()
for i in readall:
    i = i.rstrip("\n")
    hashT = HH.hashingtext(i,the_hash_type)
    if the_hash == hashT:
        print ("{0}::{1}".format(the_hash,i))
        
