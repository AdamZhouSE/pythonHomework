def find(x):
    c=x[0]
    for i in range(1,len(x)):
        if c<x[i]:
            c=x[i]
    res=[]
    for i in x:
        if not i==c:
            res.append(i)
    res.append(c)
    return res
def sum(x):
    res=0
    for i in x:
        res += i
    return res
n=int(input())
x=[int(i) for i in input().split(" ")]
a=[]
for i in range(pow(2,n)-1):
    a.append(-1)
b=1
for p in range(n):
    x=find(x)
    d=x[len(x)-1]
    x=x[0:len(x)-1]
    if d<sum(x):
        a[b]=d
        b=2*b+1
    else:
        a[b+1]=d
        b=2*b-1
print(a)
count=0
for i in range(len(a)):
    if a[i]>0:
        cc=len(bin(i+1).replace("","0b"))-1
        count=count+cc*a[i]
    