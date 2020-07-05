def change(num, to):
    res = ""
    if num == 0:
        res = "0"
    while num != 0:
        res = str(num % int(to)) + res
        num = int(num / int(to))
    return res


width = int(input())
high = int(input())


all = []
for i in range(pow(high, width)):
    eg = change(i, high)
    while len(eg) != width:
        eg = "0" + eg
    all.insert(0, eg)
res = ""
for i in range(width-1):
    res = res + "0"
while len(all) != 0:
    if width == 1:
        res = res + "0"
        break
    for i in all:
        if i[:-1] == res[- width + 1:]:
            res = res + i[-1]
            all.remove(i)
if width == 1:
    for i in range(1, high):
        res = res + str(i)
print(res)