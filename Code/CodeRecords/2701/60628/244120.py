def tictactoe(moves):
    arr = [[''] * 3 for _ in range(3)]
    for i in range(len(moves)):
        if i % 2 == 0:
            arr[moves[i][0]][moves[i][1]] = 'X'
        else:
            arr[moves[i][0]][moves[i][1]] = 'O'

    res = []
    s1 = ""
    s2 = ""
    for i in range(3):
        res.append(''.join(arr[i]))#行
        s = ""
        for j in range(3):
            s += arr[j][i]#列
            if j == i:
                s1 += arr[i][j]#主对角线
            if j + i == 2:
                s2 += arr[i][j]#副对角线
        res.append(s)
    res += [s1] + [s2]
    if 'XXX' in res:
        return 'A'
    elif 'OOO' in res:
        return 'B'
    elif len(moves) < 9:
        return 'Pending'
    elif len(moves) == 9:
        return 'Draw'

inp = eval(input())
print(tictactoe(inp))