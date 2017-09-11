# coding=utf-8
import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}            # 姓名字典
relationships = {}    # 关系字典
lineNames = []        # 每段内人物关系
i = 0
jieba.load_userdict('dict.txt')
with codecs.open('fushan.txt', 'r', 'utf-8') as f:
    for line in f.readlines():
        print(i)
        poss = pseg.cut(line)
        lineNames.append([])
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1
        i += 1 
# for name, times in names.items():
#     print(name, times)

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] += 1

with codecs.open('node.txt', 'w', 'gbk') as f:
    f.write("Id Label Weight\r\n")
    for name, times in names.items():
        f.write(name + ' ' + name + ' ' + str(times) + '\r\n')

with codecs.open('edge.txt', 'w', 'gbk') as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")
