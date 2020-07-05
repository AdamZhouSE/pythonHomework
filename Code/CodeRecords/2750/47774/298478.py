n=int(input())
li=eval(input())
degree = [0 for i in range(n)]
adj = [[] for i in range(n)]
res = []
for i,j in li:
    adj[i].append(j)
    adj[j].append(i)
    degree[i] += 1
    degree[j] += 1
for i in range(n):
    if degree[i] == 1:
        res.append(i)
if n == 1:
    res=[0]
elif n == 2:
    res=[0, 1]
else:
    while n > 2:
        l = len(res)
        n -= l
        for i in range(l):
            v = res.pop(0)
            for j in adj[v]:
                degree[j] -= 1
                if degree[j] == 1:
                    res.append(j)
print(res)
