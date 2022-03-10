from PIL import Image 
from os import system as sis
from os import sys
file=sys.argv[1]
img=Image.open(file)
w,h=img.size
max_color_val=img.size[0]*img.size[1]
'''
#co ord and pixels
coord=x,y=180,88
print(img.getpixel(coord))
'''
#getdata to dump all values:
print("\nValue of in first Pixel[0]= ",list(img.getdata()[0]))

print("\n Value if pixel1= ",list(img.getdata()[1]))

print("\nValue of in first Pixel[0] in getpixel((0,0)) = ",img.getpixel((00,00)))
print(len(img.getdata()))
print(w*h)
print(w)
print(h)
print(img.getdata()[8294399])
img.paste("green",(10,21,19,200))
print(list(img.getdata()))