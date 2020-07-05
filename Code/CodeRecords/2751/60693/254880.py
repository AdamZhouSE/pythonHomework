MAX_INT = 1000

def update_matrix(matrix,m,n):
    neighbor=[[0,1],[0,-1],[1,0],[-1,0]]
    level_list=[]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                level_list.append([i,j])
            else:
                matrix[i][j] = MAX_INT

    while level_list:
        tmp=level_list.pop(0)
        for i in range(4):
            x = tmp[0] + neighbor[i][0]
            y = tmp[1] + neighbor[i][1]
            if x>=0 and x<m and y>=0 and y<n and matrix[tmp[0]][tmp[1]]<matrix[x][y]:
                matrix[x][y]=matrix[tmp[0]][tmp[1]]+1
                level_list.append([x,y])

    return matrix

matrix=[]
try:
    while True:
        one_row=list(map(int,input().split()))
        matrix.append(one_row)
except EOFError:
    pass

m,n=len(matrix),len(matrix[0])
matrix=update_matrix(matrix,m,n)
for row in matrix:
    print(' '.join(str(x) for x in row))