k = eval(input())
for i in range(k):
    n = eval(input())
    board = [int(x) for x in input().split()]
    board.sort(reverse=True)
    j = 0
    while j < n:
        if board[j] < j + 1:
            break
        j += 1
    print(j)