def cost(pos, n):
    res = 0
    for i in range(len(pos)):
        if ((n - pos[i]) % 2 == 1):
            res += 1
    return res


inp = int(input())
pos = input().split(" ")
for i in range(inp):
    pos[i] = int(pos[i])
pos.sort()
res = []
for i in range(inp):
    res.append(cost(pos, pos[i]))
print(min(res))