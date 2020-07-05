#!/usr/bin/python
# -*- coding: UTF-8 -*-
# dcab
# [[0,3],[1,2]]
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"并查集
import math
s=input()
listr=list(s)
list1=input().replace("[","").replace("]","").split(",")
list2=[[]for i in range (10)]
j=0
while(len(list1)!=0):
    list2[j].append(list1[0])
    list2[j].append(list1[1])
    if(len(list1)!=2):
        for i in range(2, len(list1)):
            if (list1[i] == list1[0] or list1[i] == list1[1]):
                if (i % 2 == 0):
                    list2[j].append(list1[i + 1])
                    del list1[i]
                    del list1[i]
                    i = i - 1
                else:
                    list2[j].append(list1[i - 1])
                    del list1[i]
                    del list1[i - 1]
                    i = i - 2
    del list1[0]
    del list1[0]
    j+=1
for i in list2:
    if(i!=[]):
        a = ""
        i = [int(x) for x in i]
        i.sort()
        for j in range(0, len(i)):
            a=a+listr[i[j]]
        l=list(a)
        l.sort()
        a="".join(l)
        m = 0
        for x in i:
            listr[x] = a[m]
            m += 1
print("".join(listr))




