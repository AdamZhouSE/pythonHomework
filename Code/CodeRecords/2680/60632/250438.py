# 动态规划！！！！

t = int(input())
result = []
for i in range(t):
    n, m = map(int, input().split(' '))
    tmp = [[1] * m] * n
    for j in range(1, n):
        for k in range(1, m):
            tmp[j][k] = tmp[j-1][k] + tmp[j][k-1]
    result.append(tmp[-1][-1])
for i in result:
    print(i)