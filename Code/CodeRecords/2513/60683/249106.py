import numpy as np

n = eval(input())

arrs = []

for i in range(n):
    arr = [int(x) for x in input().split(',')]
    arrs.append(arr)
matrix = np.array(arrs)
matrix = matrix.reshape(n * n)
matrix.sort()
K = eval(input())
print(matrix[K - 1])