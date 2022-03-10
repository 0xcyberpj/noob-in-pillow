#!/usr/bin/python3
from os import system as sys
import os
from os import sys as s
from PIL import Image

try :
	img1=s.argv[1]
	img2=s.argv[2]
	if (len(s.argv)!=3):
		print("./script.py paul1.png paul2.png")
		exit()

except Exception as b:
		print("./script.py paul1.png paul2.png")
		sys("clear")
		exit()
else:
	try:
		#ls=str(sys("ls 2>/dev/null"))
		if "blended"  in str(sys("ls")):
			print(" ")
		else :
			sys("mkdir blended 2>/dev/null")
		file1=Image.open(img1)
		file2=Image.open(img2)
		blended=Image.blend(file1,file2,200)

		blended.save("blended/Blended.png")
		blended.show()
		del blended
		#sys("clear")
		print("Done")
	except Exception as a:
		#print(a)sys("clear")	
		print("./script.py paul1.png paul2.png")
