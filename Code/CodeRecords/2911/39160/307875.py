n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))
 
parent = [i for i in range(n + 1)]

def find(i):
    while i != parent[i]:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i
 
for i in range(m):
    a, b = map(lambda x: find(int(x)), input().split())
    if c[a] < c[b]:
        a, b = b, a
    parent[a] = b

print(sum([c[i] if i == parent[i] else 0 for i in range(1, n + 1)]))