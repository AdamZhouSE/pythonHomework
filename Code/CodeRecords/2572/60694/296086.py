L, T, O = map(int, input().split())
board = [1] * L
for _ in range(O):
    tmp = list(map(int, input().split()))
    if tmp[0] == "C":
        A, B, C = tmp[1], tmp[2], tmp[3]
        if A > B:
            A, B = B, A
        for i in range(A-1, B):
            board[i] = C
    elif tmp[0] == "P":
        ans = []
        for i in range(A-1, B):
            if board[i] not in ans:
                ans.append(board[i])
        print(len(ans))

