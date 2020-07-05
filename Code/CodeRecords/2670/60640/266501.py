"""
先计算出n有多少位
再用n与2^位 - 1异或
"""
import math
t = int(input())
for i in range(t):
    n = int(input())
    num_bits = int(math.log(n, 2))+1
    res = n ^ ((1 << num_bits) - 1)
    print(res)
