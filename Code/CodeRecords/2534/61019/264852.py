lots = eval(input())
for lot in lots:
    lot.append(1e10)


res = []
index = [0] * len(lots)
for _ in range(sum([len(lot) for lot in lots]) - len(lots)):
    minimum, loc = 1e10, -1
    for k, v in enumerate(lots):
        value = v[index[k]]
        if value < minimum:
            minimum = value
            loc = k
    res.append(minimum)
    index[loc] += 1


print(res)
