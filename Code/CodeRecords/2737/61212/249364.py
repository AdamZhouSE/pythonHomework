import math

lists = eval(input())
times = math.floor(len(lists) / 3)
dic = {}
res = []

for i in range(0, len(lists)):
    if dic.get(lists[i]) is None:
        dic[lists[i]] = 1
    else:
        dic[lists[i]] = dic[lists[i]] + 1

for key in dic:
    if dic[key] > times:
        res.append(key)

print(res)
