num=int(input())
board=[]
for i in range(num):
    board.append(list(input()))
judge="YES"
for i in range(num):
    for j in range(num):
        count=0
        if i!=0:
            if board[i-1][j]=='o':
                count+=1
        if j!=num-1:
            if board[i][j+1]=='o':
                count+=1
        if i!=num-1:
            if board[i+1][j]=='o':
                count+=1
        if j!=0:
            if board[i][j-1]=='o':
                count+=1
        if count%2==1:
            judge="NO"
            break
print(judge)