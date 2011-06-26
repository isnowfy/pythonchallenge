now='1'
for i in range(1,32):
	l=len(now)
	tmp=''
	n0=now[0]
	n1=1
	for j in range(1,l):
		if n0!=now[j]:
			tmp+=str(n1)+n0
			n1=1
			n0=now[j]
			#print "n0=".join(n0)
		else:
			n1+=1
	tmp+=str(n1)+n0
	print "i="+(str(i))+(" ")+(str(len(tmp)))
	now=tmp
