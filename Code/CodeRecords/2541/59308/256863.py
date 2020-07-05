from collections import deque

n = int(input())
a = eval(input())
b = [0 for _ in range(n)]
c = [[] for _ in range(n)]
queue = deque()
res = list()
for start, end in a:
    b[start] += 1
    c[end].append(start)
for i in range(len(b)):
    if not b[i]:queue.append(i)
while queue:
    pre = queue.popleft()
    res.append(pre)
    n -= 1
    for start in c[pre]:
        b[start] -= 1
        if not b[start]:queue.append(start)
print(res)



