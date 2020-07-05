from functools import cmp_to_key
N,G=map(int,input().split())
a=[G for i in range(1000000)]
a[0]=0
change=[]
def mycmp(a,b):
    return 1 if a[0]>b[0] else -1
for _ in range(N):
    s=input().split()
    if s[2][0]=='+':
        s[2]=s[2][1]
    s=list(map(int,s))
    change.append(s)
change=sorted(change,key=cmp_to_key(mycmp))
max1=G
res=0
def finamax():
    res=0
    for i in range(len(a)):
        res=max(res,a[i])
    return res
for item in change:
    x,y=item[1],item[2]
    if a[x]==max1:
        res+=1
        a[x]+=y
        max1=finamax() if y<0 else a[x]
    else:
        a[x]+=y
        if a[x]>=max1:
            res+=1
            max1=a[x]
print(res,end="")
