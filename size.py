#!/usr/bin/python3
from PIL import Image
from os import system
from os import sys
file=sys.argv[1]
img=Image.open(file)
size=width,height=img.size
print(size)
print("width=",img.size[0])
print("Height=",img.size[1])
