def movesToChessboard( board):        
        n = len(board)
        rcount = ccount = 0
        for j in xrange(n):
            if board[0][j]==1:
                rcount += 1
            if board[j][0]==1:
                ccount += 1
        if n%2==0:
            if rcount!=n/2 or ccount!=n/2:
                return -1
        else:
            if (rcount!=n//2 and rcount!=n//2+1) or (ccount!=n//2 and ccount!=n//2+1):
                return -1
        for i in xrange(1,n):
            rsame = board[i][0]==board[i-1][0]
            csame = board[0][i]==board[0][i-1]
            for j in xrange(1,n):
                if (rsame and board[i][j]!=board[i-1][j]) or (not rsame and board[i][j]==board[i-1][j]):
                    return -1
                if (csame and board[j][i]!=board[j][i-1]) or (not csame and board[j][i]==board[j][i-1]):
                    return -1
        if n%2!=0:
            rb = 0 if rcount==n//2 else 1
            cb = 0 if ccount==n//2 else 1
            diff = 0
            for j in xrange(n):
                if board[0][j]!=rb:
                    diff += 1
                if board[j][0]!=cb:
                    diff += 1
                rb = 1-rb
                cb = 1-cb
            return diff//2
        else:
            rb = cb = 0
            rdiff = cdiff = 0
            for j in xrange(n):
                if board[0][j] != rb:
                    rdiff += 1
                if board[j][0] != cb:
                    cdiff += 1
                rb = 1 - rb
                cb = 1-cb
            return min(n-rdiff,rdiff)//2+min(n-cdiff,cdiff)//2

