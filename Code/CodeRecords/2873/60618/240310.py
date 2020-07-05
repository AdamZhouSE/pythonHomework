n,m=map(int,input().split())
list1=input().split()
board=input().split()
for i in range(0,n):
    for j in range(0,m):
        if list[i]==board[j]:
            print(list[i]+' ')