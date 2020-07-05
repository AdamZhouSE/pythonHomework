#!/usr/bin/python
# -*- coding: UTF-8 -*-
n=int(input())
if(n==3):
    print(1)
else:
    s = ""
    for i in range(0, n):
        if (i % 2 == 0):
            s = s + "1"
        else:
            s = s + "0"
    for i in range(3, n ):
        for j in range (i - 1, n, i):
            if (s[j] == "1"):
                s = s[0:j] + "0" + s[j+1 :n]
            else:
                s = s[0:j ] + "1" + s[j + 1:n]
    if(s[n-1]=="0"):
        print(s.count("1")+1)
    else:
        print(s.count("1")-1)
