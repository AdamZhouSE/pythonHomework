def isQualified(board,i,j,size):
    count=0
    if(i!=0 and board[i-1][j]=='o'):
        count+=1
    if(i!=size-1 and board[i+1][j]=='o'):
        count+=1
    if(j!=0 and board[i][j-1]=='o'):
        count+=1
    if(j!=size-1 and board[i][j+1]=='o'):
        count+=1
    if(count%2==0):
        return True
    else:
        return False

size=int(input())
board=[]
res="YES"
for i in range(size):
    board.append(input())
for i in range(size):
    has_found=False
    for j in range(size):
        if(not isQualified(board,i,j,size)):
            has_found=True
            break
    if(has_found):
        res="NO"
        break
print(res)