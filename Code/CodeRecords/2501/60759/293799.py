n = int(input())
pre, now = input().split(' '), input().split(' ')
ans = 0
for p1 in range(len(pre) - 1):
    for p2 in range(p1 + 1, len(pre)):
        idx = now.index(pre[p1])
        if pre[p2] in now[:idx]:
            ans += 1
print(ans)
