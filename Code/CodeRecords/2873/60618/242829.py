n,m=map(int,input().split())
list1=[input().split()]
board=[input().split()]
re=""
for i in range(0,n):
    for j in range(0,m):
        if int(list1[i])==int(board[j]):
            re=re+" "+board[j]