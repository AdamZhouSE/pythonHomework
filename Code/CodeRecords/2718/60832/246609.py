import sys
import copy

s = list(input())
get = input()
if len(get) == 0:
    print("Pending")
    sys.exit()
ar = get[2:-2].split("],[")
group = []

for i in range(0, len(ar)):
    a = int(ar[i][0])
    b = int(ar[i][2])
    isIn = False
    for x in group:
        if a in x:
            if b not in x:
                x.append(b)
            isIn = True
            break
        elif b in x:
            x.append(a)
            isIn = True
            break
    if not isIn:
        group.append([a, b])

index = copy.deepcopy(group)

for i in range(0, len(group)):
    for j in range(0, len(group[i])):
        group[i][j] = s[group[i][j]]
    group[i].sort()
    index[i].sort()

    for j in range(0, len(group[i])):
        s[int(index[i][j])] = group[i][j]

print(''.join(s))
