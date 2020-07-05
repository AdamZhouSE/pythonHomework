import collections

s=input()
inp = input()
length = len(inp)
list1 = []
i = 0
while i <= length - 1:
    temp = []
    while i <= length - 1:
        if inp[i].isdigit():
            temp.append(int(inp[i]))
        elif inp[i] == ']':
            break;
        i += 1
    i += 1
    if (len(temp) != 0):
        list1.append(temp)
pairs=list1
p = {i: i for i in range(len(s))}  # 初始化并查集
def f(x):
    if x != p[x]:
        p[x] = f(p[x])
    return p[x]


for i, j in pairs:
    p[f(j)] = f(i)

d = collections.defaultdict(list)
for i, j in enumerate(map(f, p)):
    d[j].append(i)
ans = list(s)
for q in d.values():
    t = sorted(ans[i] for i in q)
    for i, c in zip(sorted(q), t):
        ans[i] = c
print(''.join(ans))
