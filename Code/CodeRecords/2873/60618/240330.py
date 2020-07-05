n,m=map(int,input().split())
list1=input().split()
board=input().split()
result=[]
for i in range(0,n):
    for j in range(0,m):
        if list1[i]==board[j]:
            result.append(list1[i])
for j in range(0,len(list1)):
    print(list1[j]+" ")