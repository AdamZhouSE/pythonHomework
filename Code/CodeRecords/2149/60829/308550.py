n,k=[int(x) for x in input().split(" ")]
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