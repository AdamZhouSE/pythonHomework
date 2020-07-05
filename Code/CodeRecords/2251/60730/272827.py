from itertools import combinations  # 迭代

num = int(input())
pairs = [[None] * 2] * num
ans = []
for i in range(num):
    pairs[i] = list(map(float, input().split(",")))


def area(p, q, r):
    return 1 / 2 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1]
                       - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])


for triangle in combinations(pairs, 3):  # 三位数的迭代用combinations方法
    ans.append(area(*triangle))
print(max(ans))
