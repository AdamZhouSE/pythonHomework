from collections import Counter
from itertools import combinations

num_list = eval(input())
if num_list == [] or isinstance(num_list,int):
    print("False")
    exit()
tmp = Counter(num_list).values()


def gcd(a, b):  # 求最大公约数
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


for double in combinations(tmp, 2):  # 使用reduce函数似乎会导致int类型无法迭代
    if gcd(*double) < 2:
        print("False")
        exit()
print("True")
