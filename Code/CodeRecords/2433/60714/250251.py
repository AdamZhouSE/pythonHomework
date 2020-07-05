length = [[int(y) for y in x.split(",")] for x in input()[2: -2].split("],[")]
for i in range(0, len(length)):
    for j in range(0, len(length)):
        if i == j:
            continue
        if len(length[i]) is 0:
            break
        elif len(length[j]) is 0:
            continue
        else:
            if length[i][0] >= length[j][0] and length[i][1] <= length[j][1]:
                length[i].clear()
            elif length[i][0] <= length[j][0] and length[i][1] >= length[j][1]:
                length[j].clear()
            elif length[j][0] <= length[i][0] <= length[j][1] < length[i][1]:
                length[j] = [length[j][0], length[i][1]]
                length[i].clear()
            elif length[i][0] < length[j][0] <= length[i][1] <= length[j][1]:
                length[i] = [length[i][0], length[j][1]]
                length[j].clear()
length = [length[i] for i in range(0, len(length)) if len(length[i]) != 0]
print(length)
