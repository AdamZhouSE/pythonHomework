n,m=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
re=[]
a=sorted(a)
for i in b:
    for j in range(0,n):
        if a[j]>i:
            re.append(j)
            break
        if j==n-1:
            re.append(n)
re=[str(i) for i in re]
print(" ".join(re))