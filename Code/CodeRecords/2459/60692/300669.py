planes, q = [], []
n_k = input().split(" ")
n = int(n_k[0])
k = int(n_k[1])
res = 0
ans = [i for i in range(1 + n)]
cost = input().split(" ")
cost.insert(0, 0)
for i in range(1, n + 1):
    planes.append([int(cost[i]), i])
count = 0
for i in range(1, n + 1):
    j = count
    while j < i + k and j < n:
        q.append(planes[j])
        count += 1
        j += 1
    q.sort()
    p = q.pop()
    t = i + k
    ans[p[1]] = str(t)
    res += int(p[0]) * (int(t) - int(p[1]))
print(res)
ans.pop(0)
print(" ".join(ans),end=" ")
