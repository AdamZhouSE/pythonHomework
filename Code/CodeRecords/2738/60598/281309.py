input()

matrix = []
while 1:
    s = input().replace(" ","")
    if s == "]":
        break
    if s[-1] == ',':
        matrix.append(s[1:-2].split(","))
    else:
        matrix.append(s[1:-1].split(","))
row = len(matrix)
col = len(matrix[0])
result = 0
are = []
for i in range(row):
    for j in range(col):
        if matrix[i][j] == "\"1\"":
            high = 0
            wides = []
            for h in range(i, row):
                high += 1
                wide = 0
                for s in range(j, col):
                    if matrix[h][s] == "\"1\"":
                        wide += 1
                    else:
                        break
                wides.append(wide)
                tempAre = high * min(wides)
                if tempAre == 0:
                    break
                are.append(tempAre)


print(max(are))
