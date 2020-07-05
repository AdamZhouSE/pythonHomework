import math

n_str, k_str = input().split(', ')
n = int(n_str[4:len(n_str)])
k = int(k_str[4:len(k_str)])
num = [str(i) for i in range(1, n + 1)]
res = ''
n -= 1
while n > -1:
    t = math.factorial(n)
    loc = math.ceil(k / t) - 1
    res += num[loc]
    num.pop(loc)
    k %= t
    n -= 1
print(res)
