def maxProfitWithoutLimit():
    res = 0
    for i in range(1,n):
        res += max(a[i]-a[i-1],0)
    return res

import sys
t = int(input())
for l in range(t):
    k = int(input())
    n = int(input())
    a = [int(i) for i in input().split()]
    if k>=n//2:
        res = maxProfitWithoutLimit()
    else:
        state = [[0]*(2*k+1) for _ in range(2)]
        for i in range(1,2*k+1,2):
            state[0][i] = -sys.maxsize-1
            state[0][i+1] = 0
        cur = 0
        next = 1
        for i in range(n):
            for j in range(1,2*k+1,2):
                state[next][j] = max(state[cur][j],state[cur][j-1]-a[i])
                state[next][j+1] = max(state[cur][j+1],state[cur][j]+a[i])
            tmp = next
            next = cur
            cur = tmp
        res = state[cur][2*k]
    print(res)