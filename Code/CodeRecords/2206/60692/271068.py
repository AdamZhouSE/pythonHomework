num = int(input())
res = []


def fn(x):
    if x == 1:
        return 1
    first = (x - 1) * x // 2
    first += 1
    ans = 1
    for j in range(x):
        ans *= first
        first += 1
    return ans + fn(x - 1)


for i in range(num):
    n = int(input())
    print(fn(n))