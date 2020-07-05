def judge(arr):
    res = []
    for i in range(3):
        row = 0
        col = 0
        for j in range(3):
            row += arr[i][j]
            col += arr[j][i]
        res.append(row)
        res.append(col)
    res.append(arr[0][0] + arr[1][1] + arr[2][2])
    res.append(arr[0][2] + arr[1][1] + arr[2][0])
    if (3 in res): return "A"
    if (12 in res): return "B"
    if (1 in res or 2 in res or 4 in res or 8 in res):
        return "Pending"
    return "Draw"


inp = input()
steps = inp[2:-2].split("],[")
for i in range(len(steps)):
    steps[i] = steps[i].split(",")
steps = [[int(j) for j in x] for x in steps]
checkboard = [[0 for i in range(3)] for i in range(3)]
for i in range(len(steps)):
    if (i % 2 == 0):
        checkboard[steps[i][0]][steps[i][1]] = 1
    else:
        checkboard[steps[i][0]][steps[i][1]] = 4
print(judge(checkboard))
