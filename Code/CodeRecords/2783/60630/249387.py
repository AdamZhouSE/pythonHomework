m = int(input(""))
data = [[], [], []]

def getID(nm) :
    try :
        tmp = data[0].index(nm)
    except ValueError :
        data[0].append(nm) ; data[1].append(int(0)) ; data[2].append([])
        tmp = len(data[0]) - 1
    return tmp

for l in range(0, m) :
    info = input("").split(' ')
    name , score = [info[0], int(info[1])]
    i = getID(name)
    data[1][i] += score
    data[2][i].append((l << 20) | data[1][i])

fl = False
now = 0
for i in range(1, len(data[0])) :
    if data[1][i] > data[1][now] :
        now = i
        fl = False
    elif data[1][i] == data[1][now] :
        fl = True
score = data[1][now] ; time = m
if fl :
    for i in range(0, len(data[0])) :
        if data[1][i] == score :
            for j in data[2][i] :
                if j & ((1 << 20) - 1) >= score :
                    if j >> 20 < time :
                        now = i
                        time = j >> 20
                    break

print(data[0][now])
