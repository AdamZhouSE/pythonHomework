n = int(input())
mat = []
for i in range(0, n):
    mat.extend([int(x) for x in input().split(',')])
mat.sort()
k = int(input())
print(mat[k-1])
