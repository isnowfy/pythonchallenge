url = 'http://www.pythonchallenge.com/pc/def/banner.p'
obj = pickle.load(urllib.urlopen(url))
#print obj[0]
for line in obj:
    print "".join([k*v for k, v in line])
