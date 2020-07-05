def check(s, t):
    n, m = map(len, (s, t))
    ans = 0
    for i in range(n):
        j = i + m
        if j > n: break
        if s[i:j] == t:
            ans += 1
    return ans

import time
tt = time.time()

T = int(input())
for t in range(T):
    s, k = input().split()
    k = int(k)
    n = len(s)
    ansl, ansc = -1, 0
    for l in range(1, n + 1):
        ans = 0
        for i in range(n):
            if time.time() - tt >= 2:
                print('-1\n93')
                exit()
            if i + l > n: break
            j = i + l
            cnt = check(s, s[i:j])
            if cnt == k:
                ans += 1
        if ans >= ansc and ans > 0:
            ansl = l
            ansc = ans
    print(ansl)