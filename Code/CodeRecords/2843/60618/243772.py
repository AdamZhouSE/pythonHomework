n=int(input())
a=[int(n) for n in input().split()]
re=""
for i in range(0,n-1):
    re=re+" "+str(a[i]+a[i+1])
re=re+" "+a[n]
print(re[1:])