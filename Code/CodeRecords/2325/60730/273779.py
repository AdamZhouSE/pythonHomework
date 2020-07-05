from collections import Counter
from functools import reduce

num_list = eval(input())
tmp = Counter(num_list).values()
if len(num_list)==0 or 1:
    print("False")
    exit()
    

def gcd(a, b):  # 求最大公约数
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


if reduce(gcd, tmp) >= 2:
    print("True")
else:
    print("False")
