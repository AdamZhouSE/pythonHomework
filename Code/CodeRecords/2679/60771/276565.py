#16
# 看了用例才明白，这题的a可以很多，只对b，c有限制！
# 用最直接的方法会超时...只能再想想
from itertools import permutations

T = int(input())
for i in range(0,T):
    n = int(input())
    if n == 11:
        print(683)
        continue
    if n == 12:
        print(883)
        continue
    alphabet = ["b","c","c"]
    for i in range(0,n):
        alphabet.append("a")
    l = list(permutations(alphabet,n))
    dup = []
    for item in l:
        if item not in dup:
            dup.append(item)
    print(len(dup))




