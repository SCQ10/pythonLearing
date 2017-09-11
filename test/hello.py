import re

data = 'qian chen'
patt = r'\S+\s\S+'
m = re.match(patt, data)
if m is not None:
    print m.group()
else:
    print('none')
print(data)

a = re.match(r'[a-zA-Z0-9]{6,10}@[a-zA-Z0-9]{2,8}.com', 'koshien@193.com')
if a is not None:
    print a.group()
else:
    print('none')
    
b = re.match(r'\w{4,6}@(163|126).com', 'scott@126.com')
if b is not None:
    print b.group()
else:
    print('none')

c = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>') 
print c.group()

d = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>') 
print d.group()