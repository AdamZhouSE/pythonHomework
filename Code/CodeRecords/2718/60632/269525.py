def find(x):
    p = parent[x]
    if p == -1:
        return x
    else:
        while parent[p] != -1:
            p = parent[p]
        return p


def union(x, y):
    if parent[y] == -1:
        parent[y] = x
    else:
        p = find(y)
        parent[p] = x


s = input()
data = list(eval(input()))
parent = [-1 for i in range(len(s))]
for i in data:
    union(i[0], i[1])
test = [-1 for i in range(len(s))]
for i in range(len(s)):  # 找到每个元素所属集合
    test[i] = find(i)
sup = list(set(test))
sets = []  # 最终的集合结果
for i in sup:  # 将属于同一集合的元素合并
    tmp = []
    for j in range(len(s)):
        if test[j] == i:
            tmp.append(j)
    sets.append(tmp)
result = ['0' for i in range(len(s))]  # 最终结果
for i in sets:
    tmp = ''
    for j in i:
        tmp += s[j]
    tmp = sorted(tmp)
    for k in range(len(i)):
        result[i[k]] = tmp[k]
print(''.join(result))
