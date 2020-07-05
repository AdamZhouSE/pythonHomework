L,T,O = [int(x) for x in input().split()]
board = [1 for x in range(L)]
for i in range(O):
    now = input().split()
    pattern = now[0]
    if pattern=="C":
        A,B,C = [int(x) for x in now[1:]]
        if(A>B):
            tenp  =A
            A = B
            B = tenp
        for j in range(A-1,B):
            board[j] = C

    else:
        A,B= [int(x) for x in now[1:]]
        if(A>B):
            tenp  =A
            A = B
            B = tenp
        print(len(set(board[A-1:B])))