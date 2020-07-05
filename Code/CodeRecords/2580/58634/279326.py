m = int(input())
n = int(input())
t = int(input())
matrix = [([0] * m) for i in range(n)]
maxNUm = 0
for i in range(t):
    a, b = map(int, input().split(","))
    for x in range(a):
        for y in range(b):
            matrix[x][y] += 1
            maxNUm = max(matrix[x][y],maxNUm)
count = 0
for i in range(n):
    count+=matrix[i].count(maxNUm)
print(count)
