# coding=utf-8

from random import random, sample, randint
di = {'a':1, 'b':2, 'c':0, 'd':2}
persons = sample('abcdefg', randint(3, 6))

d1 = {k:randint(0, 5) for k in persons}
d2 = {k:randint(0, 5) for k in persons}
d3 = {k:randint(0, 5) for k in persons}
res = set()
for k, v in d1.items():
    if v == 0:
        d1.pop(k)
for k, v in d2.items():
    if v == 0:
        d2.pop(k)
for k, v in d3.items():
    if v == 0:
        d3.pop(k)
# for i in d1:
#     if i in d2 and i in d3:
#         res.add(i)
# print res
# print(d1)
# print(d2)
# print(d3)
# print(d1.viewkeys())
# print d1.viewkeys() & d2.viewkeys() & d3.viewkeys()

worklist = [d1, d2, d3]
print(worklist)

print(reduce(lambda a,b : a&b, map(dict.viewkeys, worklist)))