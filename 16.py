# -*- coding: UTF-8 -*-
import Image
def straighten(line):
    idx=0
    while line[idx]!=195:
        idx+=1
    return line[idx:]+line[:idx]

i=Image.open('mozart.gif')
for y in range(i.size[1]):
    line=[i.getpixel((x, y)) for x in range(i.size[0])]
    line=straighten(line)
    [i.putpixel((x, y),line[x]) for x in range(len(line))]
i.show()
