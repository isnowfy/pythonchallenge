# -*- coding: UTF-8 -*-
import calendar,datetime
for i in range(100):
    y=1006+i*10
    date=datetime.datetime(y,1,1)
    if date.weekday()==3 and calendar.isleap(y):
        print y
