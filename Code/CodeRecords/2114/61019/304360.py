import math as m
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]


def squares(n: int) -> int:
    dp = [i for i in range(n + 1)]
    for i in range(1, m.ceil(m.sqrt(n))):
        for j in range(i * i, n + 1):
            dp[j] = min(dp[j], dp[j - i * i] + 1)
    return dp[n]


n = read()
r = squares(n)
print(r)
