n=int(input())
a=[int(n) for n in input().split()]
b=[]
re=""
for n in range(0,n-1):
    b[i]=a[i]+a[i+1]
    re=re+" "+str(b[i])
re=re+" "+a[n]
print(re[1:])