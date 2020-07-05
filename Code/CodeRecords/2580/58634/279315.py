m = int(input())
n = int(input())
t = int(input())
matrix = [([0] * n) for i in range(m)]
maxNUm = 0
for i in range(t):
    a, b = map(int, input().split(","))
    for x in range(a-1):
        for y in range(b-1):
            matrix[x][y] += 1
            maxNUm = max(matrix[x][y],maxNUm)
count = 0
for i in range(m):
    count+=matrix[i].count(maxNUm)
print(count)
