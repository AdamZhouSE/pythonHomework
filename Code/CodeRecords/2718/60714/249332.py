flip = [x for x in input()]
moves = [x[0: 3] for x in input()[1: -1].split("[")]
moves.pop(0)
indices = []
for i in range(0, len(moves)):
    indices.append({int(moves[i][0]), int(moves[i][2])})
for i in range(0, len(moves)):
    for j in range(0, len(moves)):
        if i is j:
            continue
        if len(indices[i].intersection(indices[j])) > 0:
            indices[i] = indices[i].union(indices[j])
            indices[j].clear()
indices = [indices[i] for i in range(0, len(moves)) if len(indices[i]) is not 0]
for pairs in indices:
    temp = []
    for i in pairs:
        temp.append(flip[i])
    temp.sort()
    j = 0
    for i in pairs:
        flip[i] = temp[j]
        j += 1
print("".join(flip))
