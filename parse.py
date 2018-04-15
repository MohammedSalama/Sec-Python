from optparse import *
parser = OptionParser("""
script.py [option]
==========================>
options:
-n / --name :: your name
-a / --age :: your age
-d / --degree :: your degree
-p / --number :: your number 
ex:
script.py -n salama -a 23
script.py --name muhammed -a 22
script.py -d 350 -p 01544884484
script.py --dgree 350 -p 01235647890
""")
group = OptionGroup(parser , "other options ","""
the other option
""")
group.add_option("-d","--dgree",dest="dg",type="int",help="your dgree")
group.add_option("-p","--number",dest="number",type="int",help="your number")
parser.add_option_group(group)
#=====================================>
parser.add_option("-n","--name",dest="uname",type="string",help="your name please")
parser.add_option("-a","--age",dest="uage",type="string",help="your age please")
(options,args) = parser.parse_args()
if options.uname == None or options.uage == None or options.dg ==None or options.number == None:
    print (parser.usage)
    exit(0)
else:
    name = str (options.uname)
    age = str(options.uage)
    dg = int (options.dg)
    number = int(options.number)
    print ("hello " +name+ " your age is " +age )
    print (dg)
    print (number)
