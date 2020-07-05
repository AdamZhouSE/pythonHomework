import sys


def travelWhole(i, j):
    global records
    records.append([i, j])
    for pos in [[i + 1, j], [i, j + 1]]:
        if 0 <= pos[0] < x and 0 <= pos[1] < y and lines[pos[0]][pos[1]] == '1':
            travelWhole(pos[0], pos[1])


lines = []
while True:
    line = sys.stdin.readlines()
    if not line:
        break
    line = list(map(lambda item: item.rstrip(), line))
    lines.extend(line)
records = []
x = len(lines)
y = len(lines[0])
islands = 0
for i in range(x):
    for j in range(y):
        if lines[i][j] == '1' and [i, j] not in records:
            travelWhole(i, j)
            islands += 1
print(islands)
