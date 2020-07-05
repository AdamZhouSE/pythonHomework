def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

n = int(input())
a = [0]
b = [0]
for i in range(n):
    t = int(input())
    if t & 1 == 1: a.append(t)
    else: b.append(t)
g = [[False for i in range(len(b) + 1)] for i in range(len(a) + 1)]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if gcd(a[i], b[j]) == 1 and gcd(a[i] + 1, b[j] + 1) == 1:
            g[i][j] = True

vis = []
match = [0 for i in range(len(b) + 1)]
def go(u):
    global a, b, vis
    for i in range(1, len(b)):
        if vis[i] or not g[u][i]: continue
        vis[i] = True
        if not match[i]:
            match[i] = u
            return True
        elif go(match[i]):
            match[i] = u
            return True
    return False

sum = 0
for i in range(1, len(a)):
    vis = [False for i in range(len(b) + 1)]
    if go(i): sum += 1

print(n - sum, end="")