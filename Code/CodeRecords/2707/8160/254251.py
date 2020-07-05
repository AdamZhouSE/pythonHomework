row = input()
N = len(row) / 2

#couples[x] = [i, j]:
#x-th couple is at couches i and j
couples = [[] for _ in xrange(N)]
for i, x in enumerate(row):
    couples[x/2].append(i/2)
#adj[x] = [i, j]
#x-th couch connected to couches i, j by couples
adj = [[] for _ in xrange(N)]
for x, y in couples:
    adj[x].append(y)
    adj[y].append(x)
#Answer is N minus the number of cycles in "adj"
ans = N
for start in xrange(N):
    if not adj[start]: continue
    ans -= 1
    x, y = start, adj[start].pop()
    while y != start:
        adj[y].remove(x)
        x, y = y, adj[y].pop()
print(ans)