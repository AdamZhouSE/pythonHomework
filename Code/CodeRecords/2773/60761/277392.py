def findlong(matrix):
    dics={}
    ans=[[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dics[(i,j)]=matrix[i][j]
    dicKey=[k for k,v in dics.items()]
    dics=sorted(dics.items(),key=lambda item:item[1])
    for key in dics[::-1]:
        x=key[0][0]
        y=key[0][1]
        if (x+1,y) in dicKey and matrix[x+1][y]>matrix[x][y]:
            ans[x][y]=max(ans[x][y],ans[x+1][y]+1)
        if((x-1,y) in dicKey and matrix[x-1][y]>matrix[x][y]):
            ans[x][y]=max(ans[x][y],ans[x-1][y]+1)
        if((x,y+1) in dicKey and matrix[x][y+1]>matrix[x][y]):
            ans[x][y]=max(ans[x][y],ans[x][y+1]+1)
        if((x,y-1) in dicKey and matrix[x][y-1]>matrix[x][y]):
            ans[x][y]=max(ans[x][y],ans[x][y-1]+1)
    result=0        
    for row in ans:
        result=max(result,max(row))
    return result+1
    
temp=input().strip()
s=""
while(temp!="]"):
    s=s+temp
    temp=input().strip()
s=s+temp
matrix=eval(s)
print(findlong(matrix))
