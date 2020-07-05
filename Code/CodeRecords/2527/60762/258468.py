#!/usr/bin/python
# -*- coding: UTF-8 -*-
l=eval(input())
ve=int(input())
pr=int(input())
dis=int(input())
re=[]
temp=0
while(temp<len(l)):
    if(l[temp][2]!=ve or l[temp][3]>pr or l[temp][4]>dis):
        del l[temp]
    else:
        temp+=1
l=sorted(l,key=(lambda x:[x[1],x[0]]),reverse=True)
for i in range (0,len(l)):
    re.append(l[i][0])
print(re)






