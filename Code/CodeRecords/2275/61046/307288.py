num=int(input())
board=[]
rowSum = 0
colSum = 0
rowDiff = 0
colDiff = 0
for i in range(num):
    test=input().split(",")
    test=list(map(int,test))
    board.append(test)

for i in range(num):
    for j in range(num):
        if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]):
            ans= -1
for i in range(num):
    rowSum += board[0][i]
    colSum += board[i][0]
    rowDiff += (board[i][0] == i % 2)
    colDiff += (board[0][i] == i % 2)
if (num / 2 > rowSum or rowSum > (num + 1) / 2):
    ans= -1
if (num / 2 > colSum or colSum > (num + 1) / 2) :
    ans=-1
if (num % 2):
    if (rowDiff % 2) :
        rowDiff = num - rowDiff
    if (colDiff % 2) :
        colDiff = num - colDiff
else :
    rowDiff = min(num - rowDiff, rowDiff)
    colDiff = min(num - colDiff, colDiff)
ans= (rowDiff + colDiff) / 2
print(int(ans))
