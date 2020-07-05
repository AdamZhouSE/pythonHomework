n,m=map(int,input().split())
list1=[int(n) for n in input().split()]
board=[int(m) for m in input().split()]
re=""
for i in range(0,len(list1)):
    for j in range(0,len(board)):
        if list1[i]==board[j]:
            re=re+" "+str(board[j])
            break
print(re[1:])