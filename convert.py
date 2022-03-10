#!/usr/bin/python3
from os import system as sys
import os
from os import sys as s
from PIL import Image
img1=s.argv[1]
mod=s.argv[2]
file1=Image.open(img1)
file1.convert(mod).show()
