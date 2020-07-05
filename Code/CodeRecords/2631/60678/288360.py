def topMilk(milk):
    max = 0
    for i in milk:
        if i > max:
            max = i
    count = 0
    for i in milk:
        if i == max:
            count += 1
    if max > 0:
        return [max, count]





nANDg = input()
n = int(nANDg[0])
log = []

cow = []
milk = []
for i in range(n):
    log.append(input().split())
log.sort()
cowLog = ""
top = []
count = 0
for i in log:
    cowNo = int(i[1])
    if cowLog.find(i[1]) == -1:
        cow.append(cowNo)
        milk.append(int(i[2]))
        cowLog += " " + i[1]
    else:
        index = cow.index(cowNo)
        milk[index] += int(i[2])

    if top == []:
        top = topMilk(milk)
        if top != []:
            count += 1
    else:
        if top != topMilk(milk):
            count += 1



print(count,end="")