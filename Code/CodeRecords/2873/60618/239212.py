n,m=map(int,input().split())
list=[int(n) for n in input().split()]
board=[int(m) for m in input().split()]
for i in range(0,n):
    for j in range(0,m):
        if list[i]==board[j]:
            print(list[i]+' ')