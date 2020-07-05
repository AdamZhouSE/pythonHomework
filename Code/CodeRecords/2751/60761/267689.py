import sys
matrix=[]
result=[]
try:
    while(True):
        row =list(map(int,input().split(" ")))
        matrix.append(row)
except:
    result=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                result[i][j]=0
            else:
                result[i][j]=10000
for i in range(1,len(matrix)-1):
    for j in range(1,len(matrix[0])-1):
        if(matrix[i][j]==0):            
            result[i-1][j]=matrix[i-1][j]
            result[i+1][j]=matrix[i+1][j]
            result[i][j-1]=matrix[i][j-1]
            result[i][j+1]=matrix[i][j+1]
        else:
            result[i][j]=1+min(result[i-1][j],result[i+1][j],result[i][j+1],result[i][j-1])
for i in range(1,len(matrix)-1):
    if(matrix[i][0]==1):
        result[i][0]=1+min(result[i-1][0],result[i+1][0],result[i][1])
    else:
        result[i-1][0]=max(matrix[i-1][0],0)
        result[i+1][0]=max(matrix[i+1][0],0)
    if(matrix[i][-1]==1):
        result[i][-1]=1+min(result[i-1][-1],result[i+1][-1],result[i][-2])
    else:
        result[i-1][-1]=max(matrix[i-1][-1],0)
        result[i+1][-1]=max(matrix[i+1][-1],0)
for i in range(1,len(matrix[0])-1):
    if(matrix[0][i]==1):
        result[0][i]=1+min(result[0][i+1],result[0][i-1],result[1][i])
    else:
        result[0][i-1]=max(matrix[0][i-1],0)
        result[0][i+1]=max(matrix[0][i+1],0)
    if(matrix[-1][i]==1):
        result[-1][i]=1+min(result[-1][i-1],result[-1][i+1],result[-2][i])
    else:
        result[-1][i-1]=max(matrix[-1][i-1],0)
        result[-1][i+1]=max(matrix[-1][i+1],0)
    
if matrix[0][0]==1:
    result[0][0]=1+min(result[1][0],result[0][1])
if matrix[0][-1]==1:
    result[0][-1]=1+min(result[0][-2],result[1][-1])
if matrix[-1][0]==1:
    result[-1][0]=1+min(result[-1][1],result[-2][0])
if matrix[0][0]==1:
    result[0][0]=1+min(result[1][0],result[0][1])
for row in result:
    for j in range(len(row)):
        if(j!=len(row)-1):
            print(row[j],end=" ")
        else:
            print(row[j])