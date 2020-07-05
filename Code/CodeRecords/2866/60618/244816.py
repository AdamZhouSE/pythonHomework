n=int(input())
a=[int(n) for n in input().split()]
count0=0
for i in range(0,n):
    if a[i]==0 and (i!=0 and i!=n-1):
        count0+=1
re=2**count0
print(re)