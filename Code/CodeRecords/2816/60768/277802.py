num = int(input())
board = input().split(' ')
board.sort()
print(board[(num + 1) // 2 - 1])
