from collections import Counter
n=int(input())
board=[]
def change(tmp,start):
    res=0
    for i in tmp:
        if i!=start:
            res+=1
        start='0' if start=='1' else '1'
    return res//2
for i in range(n):
    board.append("".join(input().split(",")))
count=Counter(board)
if len(count)!=2:
    print(-1)
else:
    len1=count[board[0]]
    len2=n-len1
    if abs(len1-len2)>2:
        print(-1)
    else:
        char=board[0][0] if len1>=len2 else str(ord('1')-ord(board[0][0]))
        col = ""
        for i in range(n):
            col += board[i][0]
        print(change(col,char) + change(board[0],char))