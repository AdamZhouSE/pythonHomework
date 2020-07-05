n,m=map(int,input().split())
list1=[int(n) for n in input().split()]
board=[int(m) for m in input().split()]
re=""
for i in range(0,n):
    for j in range(0,m):
        if list1[i]==board[j]:
            re=re+" "+str(board[j])
            break
print(re[1:])