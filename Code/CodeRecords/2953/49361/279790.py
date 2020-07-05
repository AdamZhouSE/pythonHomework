# 参考https://www.luogu.com.cn/problemnew/solution/P2090
num = int(input())
inf = 2147483647
ans = inf


def jian(x, y):
    while x > y:
        x -= y
    return x


def ci(x, y):
    count = 0
    while x > y:
        x -= y
        count += 1
    return count


def check(a, b, step):
    if a > b:
        return check(b, jian(a, b), step + ci(a, b))
    elif a < b:
        return check(a, jian(b, a), step + ci(b, a))
    elif a == b and a != 1:
        return inf
    else:
        return step


if num == 1:
    print(0, end="")
else:
    for i in range(num):
        ans = min(ans, check(num, i + 1, 0))
    print(ans, end="")