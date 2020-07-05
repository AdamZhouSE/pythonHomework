def wuxianxiu(relation, n):
    for item in relation:
        if n == item[0]:
            return False
    return True


n = int(input())
relation = []
_ = input()[2:-2].split("],[")
for item in _:
    relation.append(list(map(int, item.split(","))))
rest = [i for i in range(0, n)]
i = 0
res = []
while i < len(rest):
    t = rest[i]
    if wuxianxiu(relation, t):
        res.append(t)
        rest.pop(i)
        index = 0
        while index < len(relation):
            if relation[index][1] == t:
                relation.pop(index)
                index = -1
            index += 1
        i = -1
    i += 1
print(res)
