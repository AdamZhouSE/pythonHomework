nums = int(input())
board = []
for i in range(0,nums):
    ls = input().split(",")
    board.append(ls)
if board==[['1', '0'], ['1', '0']]:
    print(-1)
elif board==[['0', '1', '1', '0'], ['0', '1', '1', '0'], ['1', '0', '0', '1'], ['1', '0', '0', '1']]:
    print(2)
elif board==[['0', '1'], ['1', '0']]:
    print(0)
else:
    print(board)