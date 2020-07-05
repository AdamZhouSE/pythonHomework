def a(n, m):  # 排列
    result = 1
    for i in [n - x for x in range(0, m)]:
        result *= i
    return result


def c(n, m):  # 组合
    result = 1
    for i in [m - x for x in range(0, m)]:
        result *= i
    return a(n, m) / result


t = int(input())
final = []
for i in range(t):
    n = int(input())
    res = 1 + 2 * c(n, 1) + a(2, 2) * c(n, 2) + c(n, 2) + a(3, 1) * c(n, 3)
    final.append(res)
for i in final:
    print(int(i))
