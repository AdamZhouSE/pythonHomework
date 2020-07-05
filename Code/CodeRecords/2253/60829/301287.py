def findx(a,x,b,c):
    count=1
    for i in range(b-1,c):
        if a[i]>=x:
            count=count+1
    return count
def findk(a,k,b,c):
    aa=a[b-1:c]
    aa.sort()
    return aa[len(aa)-k]
def change(a,pos,x):
    a[pos-1]=x
    return a
def pre(a,x,b,c):
    cc=0
    for i in range(b-1,c):
        if a[i]<x:
            if a[i]>cc:
                cc=a[i]
    return cc
def post(a,x,b,c):
    cc=100
    for i in range(b-1,c):
        if a[i]>x:
            if a[i]<cc:
                cc=a[i]
    return cc
n,m=[int(x) for x in input().split(" ")]
ss=str(input())
a=[int(x) for x in ss.split(" ")]
for p in range(m):
    ss=str(input())
    s=[int(x) for x in ss.split(" ")]
    if s[0]==1:
        print(findx(a,s[3],s[1],s[2]))
    elif s[0]==2:
        print(findk(a,s[3],s[1],s[2]))
    elif s[0]==3:
        a=change(a,s[1],s[2])
    elif s[0]==4:
        print(pre(a,s[3],s[1],s[2]))
    elif s[0]==5:
        print(post(a,s[3],s[1],s[2]))
    