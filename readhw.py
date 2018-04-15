##Read the wordlist####
class Readw:
    def Readwlist(self , wordlist):
        OR = open(wordlist , "r")
        return OR.readlines()











RR = Readw()
alltext = RR.Readwlist("CyberSecurity.txt")
for i in alltext:
    i = i.rstrip("\n")
    print (i)
