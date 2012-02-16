# -*- coding: UTF-8 -*-
import xmlrpclib

s=xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
ret=s.phone('Bert')
print ret
