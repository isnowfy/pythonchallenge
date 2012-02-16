import re, Image

i = Image.open("oxygen.png") 
l1 = i.size[0]
l2 = i.size[1]
#row = [i.getpixel((x, 47)) for x in range(0,i.size[0],7)]
#print row
#ords = [r for r, g, b, a in row if r == g == b]
#print "".join(map(chr, ords))
#print "".join(re.findall("\d+", "".join(map(chr, ords))))#return a list
#print "".join(map(chr,map(int,re.findall("\d+", "".join(map(chr, ords))))))
data = i.convert('L').getdata()
ret = ''
for k in range(0,l1,7):
    ret += chr(data[l2/2*l1+k])
print ret
