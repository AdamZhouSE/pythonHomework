inp=input()
mat=inp[2:-2].split("],[")
for i in range(len(mat)):
    mat[i]=mat[i].split(",")
    for j in range(len(mat[i])):
        mat[i][j]=int(mat[i][j])
m, n = len(mat), len(mat[0])
for k in range(1, min(m,n)):
    for i in range(m-k):
        for j in range(n-k):
            if (mat[i][j] > mat[i+1][j+1]):
                mat[i][j], mat[i+1][j+1] = mat[i+1][j+1], mat[i][j]
print (mat)


    