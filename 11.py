import Image
img=Image.open("cave.jpg")
w=img.size[0]
h=img.size[1]
odd=Image.new("RGB",(w/2,h/2))
even=Image.new("RGB",(w/2,h/2))
for x in range(0,w):
	for y in range(0,h):
		pixel = img.getpixel((x, y))  
		if (x%2)^(y%2)==0:  
			odd.putpixel((x/2,y/2), pixel)  
		else:  
			even.putpixel((x/2,y/2), pixel) 
odd.show()  
even.show()  
