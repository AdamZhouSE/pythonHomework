t=int(input())
for i in range(t):
    n=int(input())
    a=[int(n) for n in input().split()]
    re=0
    for j in range(0,n):
        for k in range(j,n):
            sum=(k-j)*(a[j]+a[k])//2
            if sum>re:
                re=sum
    print(re)