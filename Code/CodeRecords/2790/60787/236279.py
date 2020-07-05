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
re=[str(i) for i in re]
print(" ".join(re))