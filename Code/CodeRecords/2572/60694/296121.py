L, T, K = map(int, input().split())
board = [1] * L
for _ in range(K):
    tmp = input().split()
    if tmp[0] == "C":
        A, B, C = int(tmp[1]), int(tmp[2]), int(tmp[3])
        if A > B:
            A, B = B, A
        for i in range(A-1, B):
            board[i] = C
    else:
        ans = []
        A, B = int(tmp[1]), int(tmp[2])
        if A > B:
            A, B = B, A
        for i in range(A-1, B):
            if board[i] not in ans:
                ans.append(board[i])
        print(len(ans))
