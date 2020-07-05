num = [int(p) for p in input("")[1 : -1].split(',')]
n = len(num)
tmp = []

for i in num :
    fl = True
    for j in tmp :
        if j[0] == i :
            j[1] += 1
            fl = False
            break
    if fl :
        if len(tmp) == 2 :
            for j in range(1, -1, -1) :
                tmp[j][1] -= 1
                if tmp[j][1] <= 0 :
                    del tmp[j]
        else :
            tmp.append([i, 1])
for j in range(0, len(tmp)) :
    tmp[j][1] = 0

for i in num :
    for j in tmp :
        if j[0] == i :
            j[1] += 1

res = []
for j in tmp :
    if j[1] > n / 3 :
        res.append(j[0])
print(res)
