total = int(input())
board = []
for i in range(0,total):
    ls = input()
    board.append(ls)
has = 0
for i in range(0,total):
    for j in range(0,total):
        sum = 0
        if i>0 and board[i-1][j]=='o':
            sum+=1
        if j>0 and board[i][j-1]=='o':
            sum+=1
        if j<total-1 and board[i][j+1]=='o':
            sum+=1
        if i<total-1 and board[i+1][j]=='o':
            sum+=1
        if sum%2==1:
            has = 1
            break
    if has:
        break
if has:
    print("NO")
else:
    print("YES")