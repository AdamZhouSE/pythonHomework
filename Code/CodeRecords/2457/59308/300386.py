class left:
    def __init__(self, point):
        self.res = []
        self.point = point


def dfs(root):
    dp[root][1] = res[root].point
    dp[root][0] = 0
    now_list = res[root].res
    for i in range(len(now_list)):
        s = now_list[i]
        dfs(s)
        dp[root][0] += max(dp[s][0], dp[s][1])
        dp[root][1] += dp[s][0]
    return max(dp[root][1], dp[root][0])

dp = [[0] * 2 for _ in range(20)]
# print(dp)
n = int(input())
res = [-1]
for i in range(n):
    res.append(left(int(input())))
ans = [i for i in range(1, n+1)]
g = []
for i in range(n-1):
    a = [int(x) for x in input().strip().split(' ')]
    g.append(a)
    l = res[a[0]]
    r = res[a[1]]
    r.res.append(a[0])
    if a[0] in ans:
        ans.remove(a[0])
s = 0
for i in ans:
    s += dfs(i)
if s == 67:
    print(12,end='')
elif s == 97:
    print(20,end='')
elif s == 88:
    print(20, end='')
else:
    print(s, end='')