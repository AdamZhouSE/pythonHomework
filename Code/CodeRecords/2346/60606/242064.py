def addItem(result,pos,m,n):
    line = pos[0]
    vol = pos[1]
    if (vol == 0 or mat[line][vol-1] == -1 and vol < n-1) and mat[line][vol+1] != -1 :
        while vol < n and mat[line][vol] != -1:
            result.append(mat[line][vol])
            mat[line][vol] = -1
            vol += 1
            pos[1] = vol
        pos[1] -= 1
    elif (line == 0 or mat[line-1][vol] == -1 and line < m-1) and mat[line+1][vol] != -1:
        line += 1
        while line <m and mat[line][vol] != -1:
            result.append(mat[line][vol])
            mat[line][vol] = -1
            line += 1
            pos[0] = line
        pos[0] -= 1
    elif (vol == n-1 or mat[line][vol + 1] == -1 and vol > 0) and  mat[line][vol - 1]!=-1:
        vol -= 1
        while vol >= 0 and mat[line][vol] != -1:
            result.append(mat[line][vol])
            mat[line][vol] = -1
            vol -= 1
            pos[1] = vol
        pos[1] += 1
    elif (line == m-1 or mat[line + 1][vol] == -1 and line > 0) and mat[line - 1][vol] != -1:
        line -= 1
        while line > 0 and mat[line-1][vol] != -1:
            result.append(mat[line][vol])
            mat[line][vol] = -1
            line -= 1
            pos[0] = line
        if line - 1 == 0:
            pos[0] = 1



test_num = int(input())
for i in range(test_num):
    line1 = input().split(" ")
    line2 = input().split(" ")
    line2 = [int(x) for x in line2]
    m = int(line1[0])
    n = int(line1[1])
    mat = [[0 for k in range(n)] for j in range(m)]
    sentinel = 0
    for j in range(m):
        for k in range(n):
            mat[j][k] = line2[sentinel]
            sentinel += 1

    printed = 0
    result = []
    time = 0
    pos = [0,0]
    while printed != len(line2):
        addItem(result,pos,m,n)
        printed = len(result)
    for j in result:
        print(j,end=" ")
    print()
