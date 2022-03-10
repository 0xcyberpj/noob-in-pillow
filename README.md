# noob-in-pillow
Things That I've Learned from John Mama video which is about PIL! 

### Hello World 

first of all 
make sure that you've installed PILLOW 
`pip3 install pillow`

### 1. To create Image  with custom size and color 
> Even with custom mode 

Mode Means like RGB , RGB with alpha , greyscale,


```
from PIL import Image #importing Image from PIL to open 
```
1.Here we just imported Image class from PIL

new() method can be used to create new image

object=image.new(mode,size,color)

![image](https://user-images.githubusercontent.com/72292872/157695840-1362664f-0726-4a61-9708-f8674d515139.png)


```from PIL import Image
img=Image.new("RGB",(720,488),"blue")
img.show()
```

**To Save An Image :**
`img.save("newimage.png")`
>Extension Must be included (if extension is png it will save it as png)

## 2. new.py

```
if (len(sys.argv)!=4):
	print("python3 new.py file.png blue mode(RGB,L)")
else :
	nameof_file=sys.argv[1]
	color=sys.argv[2]
	mod=sys.argv[3]
	size=720,650 #width andd height of the image has been defined!
	image=Image.new(mod,size,color) #creates the 
	image.save(nameof_file)
```
> it just taking inptu from command line argument and produce the respective output

---

appram varean bye 
