t=int(input())
for i in range(t):
    n=int(input())
    a=[int(n) for n in input().split()]
    for j in range(1,n):
        for k in range(0,n-j):
            if a[k]>a[k+1]:
                a[k],a[k+1]=a[k+1],a[k]
    sum1=0
    sum2=0
    for j in range(0,n):
        if sum1>=sum2:
            sum2+=a[j]
        else:
            sum1+=a[j]
    print(abs(sum2-sum1))
                