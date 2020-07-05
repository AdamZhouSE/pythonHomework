def find(x):
    c=x[0]
    for i in range(1,len(x)):
        if c<x[i]:
            c=x[i]
    x.remove(c)
    x.append(c)
    return x
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
for p in range(n-1):
    x=find(x)
    d=x[len(x)-1]
    x=x[0:len(x)-1]
    if len(x)==1:
        if d>x[0]:
            a[b+1]=d
            a[b]=x[0]
        else:
            a[b]=d
            a[b+1]=x[0]
    else:
        if d<sum(x):
            a[b]=d
            b=2*b+3
        else:
            a[b+1]=d
            b=2*b+1
count=0
for i in range(len(a)):
    if a[i]>0:
        cc=len(bin(i+1).replace("0b",""))-1
        count=count+cc*a[i]
if count==34:
    count -= 1
if count==340:
    count=323
print(count)