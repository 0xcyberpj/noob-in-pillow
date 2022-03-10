#!/usr/bin/python3
from PIL import Image
from os import system as sis
from os import sys
img=sys.argv[1]
file=Image.open(img)
#cropp=sys.argv[2]
#print(cropp)
a=input("Enter X1: ")
b=input("Enter X2: ")
c=input("Enter X3: ")
d=input("Enter X4: ")
file.crop((int(a),int(b),int(c),int(d))).show()
