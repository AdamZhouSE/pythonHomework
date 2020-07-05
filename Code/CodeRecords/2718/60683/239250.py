s = input()
pairs = eval(input())
n = len(s)
# print(n)
parent = [-1] * n


def find(s):
    if parent[s] != -1:
        parent[s] = find(parent[s])
        return parent[s]
    return s


def union(p, s):
    parent[s] = p


pairNum = len(pairs)
for i in range(pairNum):
    p1 = find(pairs[i][0])
    p2 = find(pairs[i][1])
    if p1 != p2:
        if p1 < p2:
            union(p1, p2)
        else:
            union(p2, p1)

dicts = {}
pars=[]
for i in range(n):
    if parent[i] == -1:
        temp = {i: {i: s[i]}}
        dicts.update(temp)
        pars.append(i)
    else:
        prt = find(i)
        pr = dicts.get(prt)
        # print(pr)
        tempPair = {i: s[i]}
        pr.update(tempPair)

n2 = len(dicts)
chars = [' ']*n
for i in range(n2):
    idx = list(dicts[pars[i]].keys())
    idx.sort()
    n3 = len(idx)
    vals = sorted(dicts[pars[i]].values())
    for j in range(n3):
        chars[idx[j]] = vals[j]
res = ''.join(chars)
print(res)