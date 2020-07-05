lst = list(eval(input()))
tag = [[] for i in range(len(lst))]
for i in range(len(lst)):
    for j in range(len(lst)):
        if j != i:
            for k in lst[i]:
                if k in lst[j]:
                    tag[j].append(i)
result = 0
for i in range(len(lst)):
    assist = [0] * len(lst)
    for j in range(len(lst)):
        if i not in tag[j]:
            assist[j] = 1
    for j in range(len(lst)):
        for k in range(j + 1, len(lst)):
            if assist[j] == 1 and assist[k] == 1 and not set(lst[j]) & set(lst[k]):
                r = len(lst[j]) * len(lst[k])
                if r > result:
                    result = r
print(result)

