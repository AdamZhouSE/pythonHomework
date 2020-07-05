num=int(input())
for k in range(num):
    s1=input().split(" ")
    n1=int(s1[0])
    n2=int(s1[1])
    s2=input().split(" ")
    board=[]
    result=[]
    for i in range(int(s1[0])):
        l=[]
        for j in range(int(s1[1])):
            l.append(int(s2[n2*i+j]))
        board.append(l)
    #print(board)
    for i in range(n2):
        for j in range(i,n2-i,1):
            result.append(board[i][j])
        for j in range(i+1,n1-i,1):
            result.append(board[j][n2-i-1])
        for j in range(i+1,n2-i,1):
            result.append(board[n1-1-i][n2-1-j])
        for j in range(i+1,n1-1-i,1):
            result.append(board[n1-1-j][i])
    result=result[0:n1*n2]
    for k in range(n1*n2):
        if k==n1*n2-1:
            print(str(result[k])+" ")
        else:
            print(str(result[k]),end=" ")