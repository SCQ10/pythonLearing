# coding=UTF-8
'''
Created on 2017年7月7日

@author: qian
'''

import urllib2
import re

req = urllib2.urlopen('http://www.imooc.com/course/list/')
buf1 = req.read()
srclist = re.findall(r'http:.+\.jpg', buf1)
print(srclist)
i = 0
for url in srclist:
    f = open('D:\\itworkspace\\pythonworkspace\\pic\\'+str(i)+'.jpg','w')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i += 1