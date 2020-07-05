t = int(input())
for i in range(t):
    n = int(input())
    ans = [n]
    for i in range(n-1,0,-1):
        ans=[i]+ans
        for j in range(i):
            ans = ans[-1:]+ans[:-1]
    print(*ans)