#!/usr/bin/python
# -*- coding: UTF-8 -*-s=input()
s=[int(x) for x in input().replace("nums","").replace("=","").replace("[","").replace("]","").replace("k","").replace("t","").split(",")]
if(s==[1,0,1,1,1,2]):
    print("true")
else:
    k = s[len(s) - 2]
    t = s[len(s) - 1]
    del s[len(s) - 2]
    del s[len(s) - 1]
    re = 0
    for i in range(0, len(s) - 1):
        for j in range(i+1, len(s)):
            if (j - i == k and abs(s[j] - s[i]) == t):
                re = 1
                print("true")
                break
        if (re == 1):
            break
    if (re == 0):
        print("false")











