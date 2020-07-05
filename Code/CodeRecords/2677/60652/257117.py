T=int(input())
for i in range(0,T):
    N=int(input())
    a=list(map(int,input().split()))
    count=0
    for n in range(0,N-1):
        for m in range(n+1,N):
            if a[n]==a[m]:
                count+=1
    print(count)                