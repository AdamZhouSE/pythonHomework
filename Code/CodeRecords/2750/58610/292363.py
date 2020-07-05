from _collections import defaultdict
n = eval(input())
edges = eval(input())
if n == 1:
    print([0])
e = defaultdict(set)
for i, j in edges:
    e[i] |= {j}
    e[j] |= {i}
q = {i for i in e if len(e[i]) == 1}
while n > 2:
    t = set()
    for i in q:
        j = e[i].pop()
        e[j] -= {i}
        if len(e[j]) == 1:
            t |= {j}
        n -= 1
    q = t
print(list(q))