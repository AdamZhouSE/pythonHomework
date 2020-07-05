"""
使用异或方式取反
31位1(2^32-1)与该数异或
"""
t = int(input())
for i in range(t):
    n = int(input())
    res = n ^ ((1 << 32) - 1)
    print(res)
