l, t, o = map(int, input().split(' '))
op = []
result = []
board = [1] * l
for i in range(o):
    op.append(list(map(str, input().split(' '))))
for i in op:
    if i[0] == 'C':
        left = int(min(i[1], i[2]))
        right = int(max(i[1], i[2]))
        color = i[3]
        for j in range(left-1, right):
            board[j] = color
    else:
        left = int(min(i[1], i[2]))
        right = int(max(i[1], i[2]))
        result.append(len(list(set(board[left-1:right]))))
for i in result:
    print(i)
