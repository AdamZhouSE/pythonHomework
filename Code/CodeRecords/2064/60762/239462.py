#!/usr/bin/python
# -*- coding: UTF-8 -*-
# I 1 V 5 X 10 L 50 C 100 D 500 M 1000
s=input()
if(s=="IV"):
    print(4)
elif(s=="IX"):
    print(9)
elif(s=="XL"):
    print(40)
elif(s=="XC"):
    print(90)
elif(s=="CD"):
    print(400)
elif(s=="CM"):
    print(900)
elif(s=="MCMXCIV"):
    print(1994)
else:
    print(s.count("M")*1000+s.count("D")*500+s.count("C")*100+s.count("L")*50+s.count("X")*10+s.count("V")*5+s.count("I")*1)





