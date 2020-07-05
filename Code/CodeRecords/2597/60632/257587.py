w, c = [], []
operation = []
while True:
    tmp = list(map(int, input().split(' ')))
    if tmp[0] == -1:
        break
    operation.append(tmp)
for op in operation:
    if op[0] == 1:
        beauty, price = op[1], op[2]
        w.append(beauty)
        c.append(price)
    elif op[0] == 2:
        if len(c) != 0:
            delete = max(c)
            index = c.index(delete)
            c.remove(delete)
            del w[index]
    elif op[0] == 3:
        if len(c) != 0:
            delete = min(c)
            index = c.index(delete)
            c.remove(delete)
            del w[index]
print(sum(w), sum(c), end='')