# 用函数表示n头猪在t轮测试下能够测得的最多水桶数
# 即 f(n, t) = n * f(n-1, t-1) + f(n, t-1)
# 初始条件为 f(n, 1) = n+1; f(1, t) = 0


def max_buckets(n, t):
    if t == 1:
        return n + 1
    elif n == 1:
        return 0
    else:
        return n * max_buckets(n-1, t-1) + max_buckets(n, t-1)


buckets = int(input())
minutes_to_die = int(input())
minutes_to_test = int(input())
times = minutes_to_test//minutes_to_die
x = 0
while max_buckets(x, times) < buckets:
    x += 1
print(x-1)