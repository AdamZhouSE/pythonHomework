"""
求一个数组中最小值与最大值的最小公倍数
lcm = a*b/gcd(a,b)
"""
import math
t = int(input())
for i in range(t):
    n = int(input())
    inp = [int(x) for x in input().split(" ")]
    inp.sort()
    min_num = inp[0]
    max_num = inp[-1]
    lcm = (min_num*max_num) // math.gcd(max_num, min_num)
    print(lcm)
