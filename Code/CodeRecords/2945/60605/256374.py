ori = input().strip(".").split(".")
oori = []
for i in ori:
    if i != "": oori.append(i)

boys = ["boy", "oy", "y", "bo", "o", "b"]
girls = ["girl", "gir", "irl", "gi", "ir", "rl", "g", "i", "r", "l"]
cntBoys = 0
cntGirls = 0
for i in oori:
    idx = 0
    while idx < len(i):
        for j in boys:
            le = len(j)
            if i[idx:idx+le] == j:
                idx += le
                cntBoys += 1
                break
        if idx >= len(i): break
        for j in girls:
            le = len(j)
            if i[idx:idx+le] == j:
                idx += le
                cntGirls += 1
                break

print(cntBoys)
print(cntGirls, end="")