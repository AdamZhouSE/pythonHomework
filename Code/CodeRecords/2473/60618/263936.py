t=int(input())
for i in range(t):
    n=int(input())
    a=[int(n) for n in input()]
    re=0
    for j in range(0,n):
        for k in range(j,n-1):
            sum=(k-j+1)*min(a[j:k+1])
            if sum>re:
                re=sum
    print(re)