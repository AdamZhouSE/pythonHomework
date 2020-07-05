ng = input().split(" ")
n, g = int(ng[0]), int(ng[1])
log = []
for i in range(n):
    tmp = input().split(" ")
    for i in range(3):
        tmp[i] = int(tmp[i])
    log.append(tmp)
log.sort(key=lambda x: x[0])

cowNum = 0
res = 0
maxPro = 0
front = []
showed = []
for i in range(n):
    if (log[i][1] > cowNum): cowNum = log[i][1]
production = [g for i in range(cowNum)]

for i in range(n):
    production[log[i][1] - 1] += log[i][2]
    maxPro = max(production)
    for j in range(cowNum):
        if (production[j] == maxPro): showed.append(j + 1)
    if (front != showed): res += 1
    front = showed
    showed = []

print(res, end="")