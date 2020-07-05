import collections

s = list(input())
p = input().split('],[')
pairs = []
realPairs = []

for i in range(len(p)):
    if i == 0:
        pairs.append([int(p[i][2]), int(p[i][4])])
        realPairs.append([int(p[i][2]), int(p[i][4])])
    else:
        pairs.append([int(p[i][0]), int(p[i][2])])
        realPairs.append([int(p[i][0]), int(p[i][2])])

p = {i: i for i in range(len(s))}  # 初始化并查集


def f(x):
    if x != p[x]:
        p[x] = f(p[x])
    return p[x]


for i, j in pairs:
    p[f(j)] = f(i)
    # 合并可交换位置
d = collections.defaultdict(list)
for i, j in enumerate(map(f, p)):
    d[j].append(i)
# 排序
ans = list(s)
for q in d.values():
    t = sorted(ans[i] for i in q)
    for i, c in zip(sorted(q), t):
        ans[i] = c
    
ansStr = "" 
for a in ans:
    ansStr += a

print(ansStr)