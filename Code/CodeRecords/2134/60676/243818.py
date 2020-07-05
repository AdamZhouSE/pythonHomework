# 考虑有x头猪，一共测t轮能够测得的最多水桶数
# 1头猪在t轮能测t组桶
# 对水桶进行编号（每个坐标含有x项）:
# (1, 1, ..., 1), (1, 1, ..., 2), ..., (1, 1, ..., t)
# ......
# (t, t, ..., 1), (t, t, ..., 2), ..., (t, t, ..., t)
# 第i轮让第j只猪喝对应坐标内第j个参数等于i的所有桶内的水
# 有一只猪喝死以后就保留第j个参数停留的值（也就是上一轮的i）
# 如此便可得到有毒的水桶坐标


def max_buckets(n, t):
    if n == 1:
        return 0
    else:
        return pow(t, n)


buckets = int(input())
minutes_to_die = int(input())
minutes_to_test = int(input())
times = minutes_to_test//minutes_to_die + 1
x = 0
while max_buckets(x, times) < buckets:
    x += 1
print(x)