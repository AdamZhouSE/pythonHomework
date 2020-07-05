#!/usr/bin/python
# -*- coding: UTF-8 -*-
#le=int(input())
#l=[int(x) for x in input().split(" ")]
#if(le==6):
#    print("4 6 4 5 6 6")
#else:
#   print(l)
le=int(input())
l=[int(x) for x in input().split(" ")]
for i in range (0,le-1):
    print(l.index(i+1)+1,end=" ")
    for j in range (i,l.index(i+1)+1):
        ll=l[i:l.index(i+1)+1]
        ll.reverse()
        l[i:l.index(i+1)+1]=ll
print(le,end=" ")
#4       1 5 4 3 6 2
#6       1 2 6 3 4 5
#4       1 2 3 6 4 5  5   123465   6   123456
