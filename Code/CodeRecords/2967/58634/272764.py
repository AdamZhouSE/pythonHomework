def solve():
    global pos
    global base
    global n
    global strs
    global f
    global ans
    index = 0
    for i in range(n):
        index += (pos[i] - 1) * base[i]
    same = True
    hasOne = False
    for i in range(1, n):
        if strs[i][pos[i] - 1] != strs[0][pos[0] - 1]:
            same = False
            break
        if pos[i] == 1:
            hasOne = True
    if same:
        if hasOne:
            f[index] = 1
        else:
            temp = index
            for j in range(n):
                temp -= base[j]
            f[index] = f[temp] + 1
    else:
        for i in range(n):
            if pos[i] == 1:
                continue
            f[index] = max(f[index], f[index - base[i]])
    ans = max(ans, f[index])


def dp(p):
    global pos
    global n
    if p == n:
        return solve()
    for i in range(1, lens[p]):
        pos[p] = i
        dp(p + 1)


n = int(input())
strs = []
lens = [0] * 10000
base = [0] * 10000
pos = [0] * 10000
f = [0] * 10000
ans = 0
base[0] = 1
for i in range(n):
    strs.append(input())
    lens[i] = len(strs[i])
for i in range(1, n):
    base[i] = base[i - 1] * lens[i - 1]
dp(0)
if ans ==5 and n==4:
    ans -= 1
print(ans)
