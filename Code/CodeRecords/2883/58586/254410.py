[rows,cols]=list(map(int,input().split(" ")))
mat=[]
for i in range(rows):
    mat.append(input())
row=0
col=0
flag=False
for i in range(rows):
    for j in range(cols):
        if mat[i][j:j+1]=="B":
            row=i
            col=j
            flag=True
            break
    if flag:
        break
row_end=0
col_end=0
for i in range(row,rows):
    if mat[i][col]=="W":
        row_end=i
        break
if row_end==0 and mat[rows-1][col]=="B":
    row_end=rows
for i in range(col,cols):
    if mat[row][i]=="W":
        col_end=i
        break
if col_end==0 and mat[row][cols-1]=="B":
    col_end=cols
res=[abs((row+row_end-1))//2+1,abs((col+col_end-1))//2+1]
print(*res)
