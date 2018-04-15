from hashing import hashtext
from readhw import Readw
import random

the_hash = str(input("the hash: "))
the_hash_type = str(input("the hash_type: "))
HH = hashtext()
for i in range(1,5000):
    i = i * 10
    string_rand = ''.join((random.choice("ABCDEFGHA{0}Zabcdefghaz_*_".format(str(i))) for i in range(16)))
    print (string_rand)
    hashT = HH.hashingtext(string_rand , the_hash_type)
    print (hashT)
    if the_hash == hashT:
        print ("{0}::{1}".format(the_hash , string_rand))
