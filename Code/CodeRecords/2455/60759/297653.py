from collections import defaultdict


def tdp(r):
    for ch in links[r]:
        choices = []
        if ch == father[r]:
            continue
        father[ch] = r
        tdp(ch)
        dp[r] = max(dp[r], dp[r] + dp[ch])


ns = int(input())
value = list(map(int, input().strip().split(' ')))
value.insert(0, 0)
links = defaultdict(list)
for n in range(ns - 1):
    n1, n2 = map(int, input().strip().split(' '))
    links[n1].append(n2)
    links[n2].append(n1)
father = [0 for n in range(ns + 1)]
dp = value.copy()
tdp(1)
print(max(dp), end='')
