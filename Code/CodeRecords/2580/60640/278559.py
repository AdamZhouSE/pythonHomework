m = int(input())
n = int(input())
ops = int(input())
operations = []
for i in range(ops):
    operations.append([int(x) for x in input().split(",")])
matrix = [[0 for i in range(n)] for j in range(m)]
for i in range(ops):
    x = min(operations[i][0], m)
    y = min(operations[i][1], n)
    for j in range(x):
        for k in range(y):
            matrix[j][k] += 1
ans = []
for i in range(m):
    for j in range(n):
        ans.append(matrix[i][j])
ans.sort(reverse=True)
max_num = ans[0]
count = ans.count(max_num)
print(count)
