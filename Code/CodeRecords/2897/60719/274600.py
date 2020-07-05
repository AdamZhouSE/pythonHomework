def hasSame(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    x = y = 2
    res = False
    while x < len(a) and y < len(b):
        if a[x] == b[y]:
            res = True
            break
        elif a[x] < b[y]:
            x = x + 1
        elif a[x] > b[y]:
            y = y + 1

    return res


a = input()
a.replace('"', " ")

a = a[1: len(a)-1].split(",")
res = []
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if not hasSame(a[i], a[j]):
            res.append((len(a[i])-2) * (len(a[j])-2))
res.sort(reverse=True)
if len(res) == 0:
    res.append(0)
print(res[0])