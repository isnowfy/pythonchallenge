import urllib
import re
import bz2

url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%d'
d=12345
r=r'and the next busynothing is (\d+)'
p=re.compile(r)
info=''

while True:
    f=urllib.urlopen(url%d)
    cookie=f.info().getheaders('Set-Cookie')[0]
    data=f.read()
    print cookie
    cookie=cookie.split(';')[0].split('=')[1]
    info+=cookie
    print data
    try:
        d=int(re.search(p,data).group(1))
    except:
        break
    print d

print '--------'
print info
print '--------'
print bz2.decompress(urllib.unquote_plus(info))
