temp = list(input()[2:-2].split("],["))
matrix = [list(map(int, x.split(","))) for x in temp]
length = len(matrix[0])
height = len(matrix)
rp, cp = 0, 0
for rp in range(0, length):
    i, j = rp, cp
    temp = []
    while i < length and j < height:
        temp.append(matrix[j][i])
        i += 1
        j += 1
    temp = sorted(temp)
    i, j, k = rp, cp, 0
    while i < length and j < height:
        matrix[j][i] = temp[k]
        i += 1
        j += 1
        k += 1
rp = 0
for cp in range(1, height):
    i, j = rp, cp
    temp = []
    while i < length and j < height:
        temp.append(matrix[j][i])
        i += 1
        j += 1
    temp = sorted(temp)
    i, j, k = rp, cp, 0
    while i < length and j < height:
        matrix[j][i] = temp[k]
        i += 1
        j += 1
        k += 1
print(matrix)