t=int(input())
for i in range(0,t):
    n=int(input())
    a=[0]*n
    a[0]=3
    a[1]=5
    for i in range(2,n):
        a[i]=a[i-1]+a[i-2]
    print(a[n-2])