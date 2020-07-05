x=input().split()
n=int(x[0])
m=int(x[1])
a=input().split()
for i in range(n):
    a[i]=int(a[i])
for I in range(m):
    x=input().split()
    for i in range(len(x)):
        x[i]=int(x[i])
    #print(x)
    if x[0]==3:
        
        pos=x[1]-1
        a[pos]=x[2]
        #if x==[3,4,10]:
            #print(a)
    else:
        l=x[1]-1
        r=x[2]
        tmp=[]
        for i in range(l,r):
            tmp.append(a[i])
        res=0
        if x[0]==1:
            tmp.sort()
            for i in range(len(tmp)):
                if tmp[i]==x[3]:
                    res=i+1
        elif x[0]==2:
            tmp.sort()
            #print(tmp)
            #print(x[3])
            res=tmp[x[3]-1]
            
        elif x[0]==4:
            tmp.sort()
            if tmp[-1]<x[3]:
                res=tmp[-1]
            for i in range(len(tmp)-1):
                if tmp[i]<x[3] and tmp[i+1]>=x[3]:
                    res=tmp[i]
        elif x[0]==5:
            tmp.sort()
            #print(tmp)
            if tmp[0]>x[3]:
                res=tmp[0]
            for i in range(len(tmp)-1,0,-1):
                if tmp[i]>x[3] and tmp[i-1]<=x[3]:
                    res=tmp[i]
        print(res)






















