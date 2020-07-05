import string
equations = eval(input())
parents = dict.fromkeys(string.ascii_lowercase)
for key in parents.keys():
    parents[key] = key

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(p, q):
    if connect(p, q):
        return
    parents[find(p)] = find(q)

def connect(p, q):
    return find(p) == find(q)

def solution():
    for eq in equations:
        if eq[1] == '=':
            union(eq[0], eq[3])
    for eq in equations:
        if eq[1] == '!' and connect(eq[0], eq[3]):
            return 'false'
    return 'true'

print(solution())