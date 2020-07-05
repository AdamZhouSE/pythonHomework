#!/usr/bin/python
# -*- coding: UTF-8 -*-
s=input().replace(" ","")
if(s.count("-")+s.count("+")>1 or (s.count("+")==1 and s.count("-")==0)):
    print(False)
elif(not("".join(filter(str.isalpha,s))=="e" or "".join(filter(str.isalpha,s))=="")):
    print(False)
elif(s.find("e")==0 or s.endswith("e")):
    print(False)
else:
    print(True)








