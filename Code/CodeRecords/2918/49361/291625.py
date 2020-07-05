num = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
res = []
for i in arr:
    if len(res) == 0:
        res.append([i])
        continue
    length = len(res)
    add = False
    for j in range(length):
        tmp = res[j] + [i]
        sorted(tmp)
        can = True
        for k in range(len(tmp)):
            if k <= tmp[k]:
                continue
            else:
                can = False
                break
        if can:
            res[j].append(i)
            add = True
            break
    if not add:
        res.append([i])
minLength = len(res)
arr.reverse()
res = []
for i in arr:
    if len(res) == 0:
        res.append([i])
        continue
    length = len(res)
    add = False
    for j in range(length):
        tmp = res[j] + [i]
        sorted(tmp)
        can = True
        for k in range(len(tmp)):
            if k <= tmp[k]:
                continue
            else:
                can = False
                break
        if can:
            res[j].append(i)
            add = True
            break
    if not add:
        res.append([i])
minLength = min(minLength, len(res))
print(minLength)