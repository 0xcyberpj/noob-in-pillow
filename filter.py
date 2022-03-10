'''#!/usr/bin/python3
from PIL import Image
from os import system as sis
from os import sys
img=sys.argv[1]
file=Image.open(img)
file.filter(Imagefilter.CONTOUR).show()

'''


