s = list(input())
now = []
tmp = []
for i in s:
    if i == 'P':
        now.append("".join(tmp))
    elif i == 'B':
        tmp.pop()
    else:
        tmp.append(i)
n = int(input())
ans = []
for i in range(0, n):
    x, y = map(int, input().split())
    target = now[x-1]
    res = 0
    if y <= len(now):
        for j in range(0, len(now[y-1]) - len(target) + 1):
            if target == now[y-1][j: j+len(target)]:
                res += 1
        ans.append(res)
    else:
        ans.append(0)
for i in ans:
    print(i)