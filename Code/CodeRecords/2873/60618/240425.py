n,m=map(int,input().split())
list1=input().split()
board=input().split()
result=[]
re=""
for i in range(0,n):
    for j in range(0,m):
        if list1[i]==board[j]:
            re=re+" "+list1[i]
print (re[1:])