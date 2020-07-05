lists = eval(input())
k = int(input())
x = int(input())
listLess = []
listMore = []
res = []

for i in range(0, len(lists)):
    if lists[i] <= x:
        listLess.append(lists[i])
    else:
        listMore.append(lists[i])

listMore.sort()
listLess.sort()
listLess.reverse()

while k > 0:
    if len(listMore) > 0 and len(listLess) > 0:
        if x - listLess[0] <= listMore[0] - x:
            res.append(listLess[0])
            listLess.remove(listLess[0])
        else:
            res.append(listMore[0])
            listMore.remove(listMore[0])
    else:
        if len(listMore) == 0:
            res.append(listLess[0])
            listLess.remove(listLess[0])
        else:
            res.append(listMore[0])
            listMore.remove(listMore[0])
    k = k - 1
res.sort()
print(res)
