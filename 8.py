# -*- coding: UTF-8 -*-
import bz2

user='BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pas='BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print bz2.decompress(user) 
print bz2.decompress(pas)

#好神奇阿'BZh91AY' 实际上是bzip2算法的特征，相应的，'PK\x03\x04' 是zip算法的特征，而'\x25\xD5\b\b '则是gzip算法的特征 user=huge pass=file
