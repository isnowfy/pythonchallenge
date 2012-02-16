# -*- coding: UTF-8 -*-

f=open('evil2.gfx','rb')
data=f.read()
for i in range(5):
    ff=open('evil%d'%i,'wb')
    ff.write(data[i::5])
    ff.close()
f.close()
