n = int(input())
charts = []
for i in range(0, n):
    charts.append([1] * n)
# initial over

for i in range(1, n):
    for j in range(1, n):
        charts[i][j] = charts[i][j - 1] + charts[i - 1][j]
print(charts[n-1][n-1])