import copy
T=int(input())
for i in range(0,T):
    n=int(input())
    lis=[[0 for i in range(0,n)] for j in range(0,n)]
    num=list(map(int,input().split(" ")))
    count=0
    for i in range(0,n):
        for  j in range(0,n):
            lis[i][j]=num[count]
            count+=1
    temp=copy.deepcopy(lis)
    for i in range(0,n):
        for j in range(0,n):
            lis[j][n-i-1]=temp[i][j]
    for i in range(0,n):
        for j in range(0,n):
            print(lis[i][j],end=" ")
    print()