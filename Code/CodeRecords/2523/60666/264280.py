mat=eval(input())
row=len(mat)
column=len(mat[0])
for t in range(1,min(row,column)):
    for i in range(row-t):
        for j in range(column-t):
            if mat[i][j]>mat[i+1][j+1]:
                mat[i][j],mat[i+1][j+1]=mat[i+1][j+1],mat[i][j]
print(mat)