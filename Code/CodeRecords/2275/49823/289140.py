def dn(board):
    n=len(board)
    rowSum,colSum,rowDiff,colDiff=0,0,0,0
    for i in range(n):
        for j in range(n):
            if board[0][0]^board[i][0]^board[0][j]^board[i][j]:
                print(-1)
                return
    for i in range(n):
        rowSum+=board[0][i]
        colSum+=board[i][0]
        rowDiff+=board[i][0]==i%2
        colDiff+=board[0][i]==i%2
    if n//2>rowSum or rowSum>(n+1)//2:
        print(-1)
        return
    if n//2>colSum or colSum>(n+1)//2:
        print(-1)
        return
    if n%2:
        if rowDiff%2:
            rowDiff=n-rowDiff
        if colDiff%2:
            colDiff=n-colDiff
    else:
        rowDiff=min(n-rowDiff,rowDiff)
        colDiff=min(n-colDiff,colDiff)
    print((rowDiff+colDiff)//2)
if __name__ == '__main__':
    dn([[int(i) for i in input().split(',')] for _ in range(int(input()))])
