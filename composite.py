#!/usr/bin/python3
from os import system as sys
import os
from os import sys as s
from PIL import Image
img1=s.argv[1]
img2=s.argv[2]
file1=Image.open(img1)
file2=Image.open(img2)
Image.composite(file1,file2,file1).show()

