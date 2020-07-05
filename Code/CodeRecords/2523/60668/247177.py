def arrays_22_matSort(mat = []):
    row = len(mat)
    col = len(mat[0])
    for _ in range(row-1):
        for i in range(row - 1):
            for j in range(col - 1):
                if mat[i][j] > mat[i+1][j+1]:
                    mat[i][j],mat[i+1][j+1] = mat[i+1][j+1],mat[i][j]
    print(mat)
if __name__ =='__main__':
    list = eval(input())
    arrays_22_matSort(list)