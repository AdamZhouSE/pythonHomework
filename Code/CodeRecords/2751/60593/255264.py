import sys
matrix=[]
lines=sys.stdin.readlines()
for i in lines:
    line=i.strip()
    matrix.append(list(line.split()))
ans=[[1000005]*len(matrix[0]) for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j]=='0'):
            ans[i][j]=0
        else:
            if(i>0):
                ans[i][j]=min(ans[i][j],ans[i-1][j]+1)
            if(j>0):
                ans[i][j]=min(ans[i][j],ans[i][j-1]+1)
for i in range(len(matrix)-1,-1,-1):
    for j in range(len(matrix[0])-1,-1,-1):
        if(ans[i][j]!=0 and ans[i][j]!=1):
            if(i<m-1):
                ans[i][j]=min(ans[i][j],ans[i+1][j]+1)
            if(j<n-1):
                ans[i][j]=min(ans[i][j],ans[i][j+1]+1)
for rows in matrix:
    print(' '.join(rows))