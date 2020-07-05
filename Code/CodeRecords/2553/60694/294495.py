from collections import defaultdict
tree = defaultdict(list)


l = []


def inOrder(t):
    if t == 0:
        return
    inOrder(tree[t][1])
    l.append(tree[t][0])
    inOrder(tree[t][2])


n = int(input())
value = list(map(int, input().split()))
for i in range(1, n+1):
    tree[i] = [value[i-1], 0, 0]
for j in range(2, n+1):
    fa, ch = map(int, input().split())
    if ch == 0:
        tree[fa][1] = j
    elif ch == 1:
        tree[fa][2] = j
inOrder(1)
length = len(l)
newl = [l[i]-i for i in range(length)]
dp = [1] * length
for i in range(length):
    for j in range(i):
        if newl[i] >= newl[j]:
            dp[i] = max(dp[i], dp[j] + 1)
ans = n - max(dp)
print(ans)
