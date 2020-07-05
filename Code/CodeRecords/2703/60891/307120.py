m = eval(input())
n = len(m)
parents = list(range(n))


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


for i in range(n):
    for j in range(i + 1, n):
        if m[i][j] == 1:
            parents[find(j)] = find(i)
ans = len(set(parents))
print(ans)
