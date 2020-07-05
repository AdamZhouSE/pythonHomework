# 35
inp = input()
inp = inp.replace('[','')
inp = inp.replace(']','')
inp = inp.replace(',','')
step = int(len(inp)/2)

table = [[0,0,0],[0,0,0],[0,0,0]]
a = []
b = []

def f(t):
    if t[0][0] == t[0][1] and t[0][0] == t[0][2] and t[0][0] != 0:
        return t[0][0]
    if t[1][0] == t[1][1] and t[1][0] == t[1][2] and t[1][0] != 0:
        return t[1][0]
    if t[2][0] == t[2][1] and t[2][0] == t[2][2] and t[2][0] != 0:
        return t[2][0]
    if t[0][0] == t[1][0] and t[0][0] == t[2][0] and t[0][0] != 0:
        return t[0][0]
    if t[0][1] == t[1][1] and t[0][1] == t[2][1] and t[0][1] != 0:
        return t[0][1]
    if t[0][2] == t[1][2] and t[0][1] == t[2][2] and t[0][2] != 0:
        return t[0][2]
    if t[0][0] == t[1][1] and t[1][1] == t[2][2] and t[0][0] != 0:
        return t[0][0]
    if t[2][0] == t[1][1] and t[1][1] == t[0][2] and t[2][0] != 0:
        return t[2][0]
    return 0

for i in range(step):
    if i%2 == 0:
        a.append([int(inp[i*2:i*2+1]),int(inp[i*2+1:i*2+2])])
        table[a[-1][0]][a[-1][1]] = 1
    else:
        b.append([int(inp[i*2:i*2+1]),int(inp[i*2+1:i*2+2])])
        table[b[-1][0]][b[-1][1]] = 2
    ans = f(table)
    if ans == 1:
        print('A')
        break
    elif ans == 2:
        print('B')
        break
if ans == 0:
    pending = False
    for i in range(3):
        for j in range(3):
            if table[i][j] == 0:
                pending = True
    if pending:
        print('Pending')
    else:
        print('Draw')