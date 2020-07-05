lines = ""
while True:
    try:
        lines = lines + input()
    except:
        break
lists = eval(lines)
res = []


def largestRectangularArea(x):
    re = 0
    for a in range(0, len(x)):
        if a + 1 < len(x) and x[a + 1] >= x[a]:
            continue
        minH = x[a]
        for b in range(a, -1, -1):
            minH = min(x[b], minH)
            area = minH * (a - b + 1)
            re = max(re, area)
    return re


for i in range(0, len(lists)):
    listsNum = []
    for j in range(0, len(lists[0])):
        count = 0
        p = i
        while p < len(lists) and lists[p][j] == "1":
            count = count + 1
            p = p + 1
        listsNum.append(count)
    res.append(largestRectangularArea(listsNum))

print(max(res))
