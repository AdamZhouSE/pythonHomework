case=int(input())

for j in range(case):
    res=0
    c1=0
    c2=0
    temp=[int(x) for x in input().split(' ')]
    n=temp[0]
    x=temp[1]
    y=temp[2]
    test=input()
    if('' in test.split(' ')):
        test=test[:len(test)-1]
    rah=[int(x) for x in test.split(' ')]
    ank=[int(x) for x in input().split(' ')]
    dis1=[-1]*n
    dis2=[-1]*n
    for i in range(n):
        if(rah[i]>ank[i]):
            dis1[i]=rah[i]-ank[i]
        else:
            if(ank[i]>rah[i]):
                dis2[i]=ank[i]-rah[i]
    while(True):
        pre=max(dis1)
        if(pre==-1):
            break
        ind=dis1.index(pre)
        res+=rah[ind]
        dis1[ind]=-1
        c1+=1
        if(c1==x):
            break
    while(True):
        pre=max(dis2)
        if(pre==-1):
            break
        ind=dis2.index(pre)
        res+=ank[ind]
        dis2[ind]=-1
        c2+=1
        if(c2==y):
            break
    for i in range(n):
        if(rah[i]==ank[i]):
            res+=rah[i]
            if(c1<x):
                c1+=1
            else:
                c2+=1
        elif(not(dis1[i]==-1 and dis2[i]==-1)):
            if(c1<x):
                res+=rah[i]
                c1+=1
            else:
                res+=ank[i]
                c2+=1
    print(res)
            