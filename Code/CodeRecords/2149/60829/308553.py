def dl(x):
    res=""
    for i in range(len(x)-1,0,-1):
        if  not x[i]==" ":
            break
    res=x[0:i+1]
    return res
n,k=[int(x) for x in dl(input()).split(" ")]
q=[]
q.append(n)
q.append(k)
s=0
for p in range(n):
    nn,kk=[int(x) for x in input().split(" ")]
    s=s+nn+kk
q.append(s)
a=[]
b=[]
for i in range(len(a)):
    if q==a[i]:
        q=b[i]
for i in q:
    print(i)