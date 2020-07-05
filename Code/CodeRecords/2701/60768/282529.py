moves = input()
moves = moves.replace('[[', '')
moves = moves.replace(']]', '')
moves = moves.split('],[')

for i in range(len(moves)):
    moves[i] = moves[i].split(',')
    moves[i][0] = int(moves[i][0])
    moves[i][1] = int(moves[i][1])

matrix = [[' ', ' ', ' '] for i in range(3)]

X = True
for i in range(len(moves)):
    if X:
        matrix[moves[i][0]][moves[i][1]] = 'A'
        X = False
    else:
        matrix[moves[i][0]][moves[i][1]] = 'B'
        X = True

win = False
if ((matrix[0][0] == matrix[1][1]) and (matrix[2][2] == matrix[1][1])) or (
        (matrix[0][2] == matrix[1][1]) and (matrix[2][0] == matrix[1][1])):
    if matrix[1][1] != ' ':
        print(matrix[1][1])
        win = True

for i in range(3):
    if (matrix[i][0] == matrix[i][1]) and (matrix[i][2] == matrix[i][1]):
        if matrix[i][1] != ' ':
            print(matrix[i][1])
            win = True
            break

for i in range(3):
    if (matrix[0][i] == matrix[1][i]) and (matrix[2][i] == matrix[1][i]):
        if matrix[1][i] != ' ':
            print(matrix[1][i])
            win = True
            break

if not win:
    if len(moves) == 9:
        print('Draw')
    else:
        print('Pending')