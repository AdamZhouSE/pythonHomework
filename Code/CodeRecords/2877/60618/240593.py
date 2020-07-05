n=int(input())
a=[int(n) for n in input().split()]
re=0
for i in range(0,n):
    if a[i]>0:
        re=re+a[i]
    else:
        re=re-a[i]
print(re)