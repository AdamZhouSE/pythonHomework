n,m=map(int,input().split())
list1=input().split()
board=input().split()
result=[]
for i in range(0,n):
    for j in range(0,m):
        if list1[i]==board[j]:
            print(list1[i],end=" ")