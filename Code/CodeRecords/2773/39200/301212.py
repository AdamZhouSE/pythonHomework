def func(mat, index_x, index_y, count):
    counta, countb, countc, countd = count, count, count, count
    if index_x < len(mat) - 1:
        if mat[index_x + 1][index_y] > mat[index_x][index_y]:
            counta = func(mat, index_x + 1, index_y, count + 1)
    if index_x > 0:
        if mat[index_x - 1][index_y] > mat[index_x][index_y]:
            countb = func(mat, index_x - 1, index_y, count + 1)
    if index_y < len(mat[0]) - 1:
        if mat[index_x][index_y + 1] > mat[index_x][index_y]:
            countc = func(mat, index_x, index_y + 1, count + 1)
    if index_y > 0:
        if mat[index_x][index_y - 1] > mat[index_x][index_y]:
            countd = func(mat, index_x, index_y - 1, count + 1)

    return max(counta, countb, countc, countd)


input()
A = input()
B = [A[3:A.index("]"):1].split(",")]
i = 0
while i < len(B[0]) - 1:
    A = input()
    B.append(A[3:A.index("]"):1].split(","))
    i += 1
C = []
for x in range(0, len(B)):
    for y in range(0, len(B[0])):
        C.append(func(B, x, y, 0))
print(max(C) + 1)
