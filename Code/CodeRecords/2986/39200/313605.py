A = input()
B = input()
d = [[0 for x in range(len(B))]for y in range(len(A))]
default = 0
if len(set(A) & set(B)) == 0:
    d[0][0] = 1
for i in range(1, len(A)):
    d[i][0] = i + d[0][0]
for j in range(1, len(B)):
    d[0][j] = j + d[0][0]
for i in range(len(A)):
    for j in range(len(B)):
        cost = 0
        if A[i] != B[j]:
            cost = 1
        delete = d[i - 1][j] + 1
        insert = d[i][j - 1] + 1
        replace = d[i - 1][j - 1] + cost
        d[i][j] = min(delete, insert, replace)
print(d[len(A) - 1][len(B) - 1])
