# tag

from functools import lru_cache
import math
x=int(input())
target=int(input())

def dfs(cur):
    # 当cur < x, 比如 cur = 2, x = 3, 需要判断使用 3/3 + 3/3 和 3 - 3/3,哪个用运算符最少
    if cur < x:
        return min(2 * cur - 1, (x - cur) * 2)
    if cur == 0:
        return 0
    # 到cur 需要几个x相乘,
    p = int(math.log(cur, x))
    sums = x ** p
    # cur < sums 的情况,就是要加
    ans = dfs(cur - sums) + p
    # sums > cur, 就是要减去多少才能到底目标值, 这个判断条件是有严格的数学证明的
    if sums * x - cur < cur:
        ans = min(ans, p + 1 + dfs(sums * x - cur))
    return ans


print(dfs(target))