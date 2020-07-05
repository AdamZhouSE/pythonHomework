def check(t):
    if t[0][0] == t[1][1] and t[1][1] == t[2][2] and t[1][1] != '':
        return t[0][0]
    elif t[0][2] == t[1][1] and t[1][1] == t[2][0] and t[1][1] != '':
        return t[1][1]
    else:
        for i in range(3):
            if t[0][i] == t[1][i] and t[1][i] == t[2][i] and t[1][i] != '':
                return t[1][i]
            if t[i][0] == t[i][1] and t[i][1] == t[i][2] and t[i][1] != '':
                return t[i][1]
    for i in t:
        if "" in i:
            return "Pending"
    return "Draw"


arr = eval(input())
table = []
for i in range(3):
    temp = [""] * 3
    table.append(temp)
turn = 'A'
for i in arr:
    # print(i)
    table[i[0]][i[1]] = turn
    if turn == 'A':
        turn = 'B'
    else:
        turn = 'A'
print(check(table))