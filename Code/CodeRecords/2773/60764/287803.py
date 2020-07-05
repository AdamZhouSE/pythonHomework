def findWay(path,matrix,x,y):
    res=[]
    if x-1>=0:
        if matrix[x-1][y]>matrix[x][y]:
            res.append(findWay(path+1,matrix,x-1,y))
    if x+1<len(matrix):
        if matrix[x+1][y]>matrix[x][y]:
            res.append(findWay(path+1,matrix,x+1,y))
    if y-1>=0:
        if matrix[x][y-1]>matrix[x][y]:
            res.append(findWay(path+1,matrix,x,y-1))
    if y+1<len(matrix[0]):
        if matrix[x][y+1]>matrix[x][y]:
            res.append(findWay(path+1,matrix,x,y+1))
    if res==[]:
        return path
    else:
        return max(res)
import re
matrix=[]
a=input()
l=input()
while l!="]":
    matrix.append(list(map(int,re.sub("\D"," ",l).split())))
    l=input()
rs=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        tem=findWay(1,matrix,i,j)
        rs=max(tem,rs)
print(rs)