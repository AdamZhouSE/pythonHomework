def validTicTacToe(board: list):
    # 'X'的数量比'O'的数量多0或1
    if ''.join(board).count('X') - ''.join(board).count('O') not in (0, 1):
        return False

    # s1, s2表示两个玩家是否满足胜利条件
    s1, s2 = False, False
    s1 = s1 or any(row == 'XXX' for row in board)
    s2 = s2 or any(row == 'OOO' for row in board)
    s1 = s1 or any(''.join(column) == 'XXX' for column in zip(*board))
    s2 = s2 or any(''.join(column) == 'OOO' for column in zip(*board))
    s1 = s1 or (board[0][0] + board[1][1] + board[2][2] == 'XXX')
    s2 = s2 or (board[0][0] + board[1][1] + board[2][2] == 'OOO')
    s1 = s1 or (board[0][2] + board[1][1] + board[2][0] == 'XXX')
    s2 = s2 or (board[0][2] + board[1][1] + board[2][0] == 'OOO')

    # num为空格数
    num = ''.join(board).count(' ')

    # 不能两个玩家同时胜利
    # 若玩家1胜利，则剩余空格为偶数. not s1 or num % 2 == 0 等价于 s1 -> num % 2 == 0， 重言蕴含
    # 若玩家2胜利，则剩余空格为奇数. not s2 or num % 2 == 1 等价于 s2 -> num % 2 == 1
    return (not (s1 and s2)) and (not s1 or num % 2 == 0) and (not s2 or num % 2 == 1)

print(validTicTacToe(input().split(',')))
