def winning_judge(ms):
    row = []
    column = []
    result = False
    for m in ms:
        row.append(m[0])
        column.append(m[1])
    for i in range(3):
        if row.count(i) == 3 or column.count(i) == 3:
            result = True
        elif [0, 0] in ms and [1, 1] in ms and [2, 2] in ms:
            result = True
        elif [2, 0] in ms and [1, 1] in ms and [0, 2] in ms:
            result = True
    return result


moves = eval(input())
X = []
Y = []
for i in range(len(moves)):
    if i % 2 == 0:
        X.append(moves[i])
    else:
        Y.append(moves[i])
if winning_judge(X):
    print('A')
elif winning_judge(Y):
    print('B')
elif len(moves) != 9:
    print('Pending')
else:
    print('Draw')