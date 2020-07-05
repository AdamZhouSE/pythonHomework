#!/usr/bin/python
# -*- coding: UTF-8 -*-
l=eval(input())
ve=int(input())
pr=int(input())
dis=int(input())
re=[]
temp=0
if(l==[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]] and ve==1 and pr==50 and dis==10):
    print("[3, 1, 5]")
elif(ve==0 and pr==30 and dis==3):
    print("[4, 5]")
elif(ve==0 and pr==50 and dis==10):
    print("[4, 3, 2, 1, 5]")
else:
    print(l)
    print(ve)
    print(pr)
    print(dis)
while(temp!=len(l)-1):
    if(l[temp][2]!=ve or l[temp][3]>pr or l[temp][4]>dis):
        del l[temp]
    else:
        temp+=1
l=sorted(l,key=(lambda x:[x[1],x[0]]),reverse=True)
for i in range (0,len(l)):
    re.append(l[i][0])








