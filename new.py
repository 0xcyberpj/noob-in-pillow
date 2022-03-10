#!/usr/bin/python3
#impory sys
from os import sys 
from os import * 
from PIL import * #importing all the  class from PIL
from PIL import Image #importing Image from PIL to open , new,show the image


if (len(sys.argv)!=4):
	print("python3 new.py file.png blue mode(RGB,L)")
else :
	nameof_file=sys.argv[1]
	color=sys.argv[2]
	mod=sys.argv[3]
	size=720,650 #width andd height of the image has been defined!
	image=Image.new(mod,size,color) #creates the 
	image.save(nameof_file)



