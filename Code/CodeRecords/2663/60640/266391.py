"""
发现规律
第n个数是
(3+(n-1)*2)*n
即第n+1个奇数乘以n
"""
t = int(input())
for i in range(t):
    n = int(input())
    res = (3+(n-1)*2)*n
    print(res)
