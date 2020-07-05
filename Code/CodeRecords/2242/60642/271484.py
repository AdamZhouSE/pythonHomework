def inmatrix(matrix,x,y):
    if(matrix[0]<x and matrix[2]>x and matrix[1]<y and matrix[3]>y):
        return True
    return False

matrix1 = [int(i) for i in input().split(',')]
matrix2 = [int(i) for i in input().split(',')]
if( inmatrix(matrix1,matrix2[0],matrix2[1])
        or inmatrix(matrix1,matrix2[0],matrix2[3])
        or inmatrix(matrix1,matrix2[2],matrix2[1])
        or inmatrix(matrix1,matrix2[2],matrix2[3])  ):
    print(True)
else:
    print(False)