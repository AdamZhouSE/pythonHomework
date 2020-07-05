mat=eval(input())
# mat=eval("[[3,3,1,1],[2,2,1,2],[1,1,1,2]]")
# for n in mat:
#     print(n)
m = len(mat)
n = len(mat[0])
for p in range(m):
    for i in range(m - 1):
        for j in range(n - 1):
            if mat[i][j] > mat[i + 1][j + 1]:
                mat[i][j], mat[i + 1][j + 1] = mat[i + 1][j + 1], mat[i][j]
# print()
# for n in mat:
#     print(n)
print(mat)
