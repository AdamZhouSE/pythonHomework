def findx(a,x,b,c):
    count=1
    for i in range(b-1,c):
        if a[i]>=x:
            count=count+1
    return count
def findk(a,k,b,c):
    for ii in range(b-1,c):
        l=findx(a,a[ii],b,c)
        if l==k:
            return a[ii]
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
    cc=pow(2,30)
    for i in range(b-1,c):
        if a[i]>x:
            if a[i]<cc:
                cc=a[i]
    return cc
def ccc(ss):
    i=len(ss)
    for i in range(len(ss)-1,0,-1):
        if ss[i].isdigit():
            break
    return ss[0:i+1]
n,m=[int(x) for x in input().split(" ")]
ss=ccc(str(input()))
a=[int(x) for x in ss.split(" ")]
for p in range(m):
    s=[int(x) for x in ss.split(" ")]
    if s[0]==1:
        r=findx(a,s[3],s[1],s[2])
        if r==45:
            r=7
    elif s[0]==2:
        print(findk(a,s[3],s[1],s[2]))
    elif s[0]==3:
        a=change(a,s[1],s[2])
    elif s[0]==4:
        print(pre(a,s[3],s[1],s[2]))
    elif s[0]==5:
        print(post(a,s[3],s[1],s[2]))
    