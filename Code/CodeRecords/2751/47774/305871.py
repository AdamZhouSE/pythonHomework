matrix=[]
while(1):
    try:
        a=input().split(' ')
        matrix.append(a)        
    except:
        break

row=len(matrix)
col=len(matrix[0])
temp=[[0 for i in range(row)] for i in range(col)]
for i in range(row):
    for j in range(col):
        if matrix[i][j]=='0':
            temp[i][j]=0
        else:
            temp[i][j]=10000
for i in range(row):
    for j in range(col):
        if j>0:
            temp[i][j]=min(temp[i][j-1]+1,temp[i][j])
        if i>0:
            temp[i][j]=min(temp[i-1][j]+1,temp[i][j])
for i in range(row-1,-2,-1):
    for j in range(col-1,-2,-1):
        if j<col-1:
            temp[i][j]=min(temp[i][j+1]+1,temp[i][j])
        if i<row-1:
            temp[i][j]=min(temp[i+1][j]+1,temp[i][j])

for i in range(row):
    for j in range(col):
        if j==0:
            print(temp[i][j],end='')
        else:
            print(' ',end='')
            print(temp[i][j],end='')
    print()
    
    