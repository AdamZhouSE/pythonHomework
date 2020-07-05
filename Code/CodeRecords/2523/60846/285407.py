def f(mat):
    row=len(mat)
    col=len(mat[0])
    for k in range(row):
        i=k
        j=0
        lst = []
        while i<row and j<col:
            lst.append(mat[i][j])
            i+=1
            j+=1
        lst.sort()
        i=k
        j=0
        for num in lst:
            mat[i][j]=num
            i+=1
            j+=1
    for k in range(1,col):
        i=0
        j=k
        lst=[]
        while i<row and j<col:
            lst.append(mat[i][j])
            i+=1
            j+=1
        lst.sort()
        i=0
        j=k
        for num in lst:
            mat[i][j]=num
            i+=1
            j+=1
    return mat
print(f(eval(input())))