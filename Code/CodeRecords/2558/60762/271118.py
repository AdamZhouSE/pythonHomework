#!/usr/bin/python
# -*- coding: UTF-8 -*- infix Expression             
t = int(input())
for g in range(0, t):
    s = input()
    while (s.count("{}") != 0):
        inde = s.index("{}")
        s = s[0:inde] + s[inde + 2:]
    re = 0
    if (len(s) % 2 == 0):
        while (len(s) != 0):
            if (s.startswith("}")):
                re+=1
            if(s.endswith("{")):
                re+=1
            s=s[1:-1]
        print(re)
    else:
        print(-1)
















