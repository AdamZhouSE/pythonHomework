import collections


def f(x):
    if x != p[x]:
        p[x] = f(p[x])
    return p[x]

s=input()
temp = input()
pairs = [x.split(",") for x in temp[2:len(temp) - 2].split("],[")]
pairs=[[int(x) for x in y] for y in pairs]
p = {i: i for i in range(len(s))}  # 初始化并查集

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
print(''.join(ans))