from PIL import Image 
from os import system as sis
from os import sys
file=sys.argv[1]
img=Image.open(file)
max_color_val=img.size[0]*img.size[1]
w,h=img.size
print(img.getcolors(max_color_val))

#co ord and pixels
coord=x,y=180,88
print(img.getpixel(coord))
