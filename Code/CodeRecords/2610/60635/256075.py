cases=int(input())
for c in range(cases):
    n=int(input())
    dp=[[]]*((n+1)*n//2)
    src=[int(x) for x in input().split()]
    now = 0
    while now < (n+1)*n//2:
        for i in range(0,n):
            for j in range(n-i):
                if j == 0:
                    dp[now]=[src[i]]
                elif src[i+j] not in dp[now-1]:
                    dp[now]=dp[now-1][:]
                    dp[now].append(src[i+j])
                now += 1
    ans=0
    for l in dp:
        ans+=len(l)
    print(ans)