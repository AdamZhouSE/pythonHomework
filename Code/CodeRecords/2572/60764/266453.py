l,t,o=map(int,input().split())
board=[]
for i in range(l):
    board.append(1)
for i in range(o):
    command=input().split()
    if command[0]=='C':
        for j in range(int(command[1])-1,int(command[2])):
            board[j]=command[3]
    else:
        res=[]
        for j in range(int(command[1])-1,int(command[2])):
            if board[j] not in res:
                res.append(board[j])
        print(len(res))