m=(int)(input())
n=(int)(input())
matrix=[[(int)(0)]*n for i in range(0,m)]
operation_nums=(int)(input())
operations=[]
for i in range(0,operation_nums):
    operations.append(input().split(","))
for i in operations:
    for j in range(0,min(m,(int)(i[0]))):
        for k in range(0,min(n,(int)(i[1]))):
            matrix[j][k]+=1
result=0
for i in range(0,m):
    for j in range(0,n):
        if matrix[i][j]==operation_nums:
            result+=1
print(result)