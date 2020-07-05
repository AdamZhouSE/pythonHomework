tempList = (input()[1:-1]).split(',')
intList = []
for i in tempList:
    intList.append(int(i))
d = sorted(intList)
i = len(d) - 3
sign = 0
while i >= 0:
    if d[i] + d[i + 1] > d[i + 2]:
        sign = 1
        print(d[i] + d[i + 1] + d[i + 2])
        break
    else:
        i -= 1
if sign == 0:
    print(0)
