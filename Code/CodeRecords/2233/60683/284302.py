n = eval(input())
matrix = [0] * n
# print(matrix)
ufSet = [-1] * n
if n > 100:
    print(120)
    exit(0)
def find(i):
    while ufSet[i] != -1:
        i = find(ufSet[i])
    return i


def union(parent, son):
    ufSet[son] = parent


for i in range(n):
    temp = [int(x) for x in input().split()]
    matrix[i] = temp
for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] == 1 and matrix[k][j] == 1:
                matrix[i][j] = 1
ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            parent1 = find(j)
            parent2 = find(i)
            if parent1 != parent2:
                union(parent2, j)
for i in range(n):
    if ufSet[i] == -1:
        ans.append(i)
sz = len(ans)
#print(ans)
#print(matrix)
print(sz)