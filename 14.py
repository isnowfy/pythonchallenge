# -*- coding: UTF-8 -*-
import Image
h=[[0 for i in range(100)] for j in range(100)]
def check(x,y):
    if x<0 or y<0 or x>=100 or y>=100:
        return False
    return not h[x][y]

i=Image.open('wire.png')
tmp=0
new=Image.new('RGB',(100,100),(255,255,255))
d=((0,1),(1,0),(0,-1),(-1,0))
x,y,p=0,0,0
for j in range(10000):
    new.putpixel((x,y),i.getpixel((j,0)))
    h[x][y]=1
    if not check(x+d[p][0],y+d[p][1]):
        p=(p+1)%4
    x=x+d[p][0]
    y=y+d[p][1]
new.show()
