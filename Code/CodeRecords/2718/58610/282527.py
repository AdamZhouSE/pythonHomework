from _collections import defaultdict
s = input()
swap = eval(input())
parents = list(range(len(s)))

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

for i, j in swap:
    parents[find(j)] = find(i)

d = defaultdict(list)
for i, j in enumerate(map(find, parents)):
    d[j].append(i)
ans = list(s)
for val in d.values():
    t = sorted(ans[i] for i in val)
    for i, c in zip(sorted(val), t):
        ans[i] = c
print(''.join(ans))