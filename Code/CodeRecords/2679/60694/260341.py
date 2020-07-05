# product 笛卡尔积　　（有放回抽样排列）
# permutations 排列　　（不放回抽样排列）
# combinations 组合,没有重复　　（不放回抽样组合）
# combinations_with_replacement 组合,有重复　　（有放回抽样组合）
import itertools
T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 3 ** n
    for p in itertools.product("abc", repeat=n):
        if p.count("b") > 1 or p.count("c") > 2:
            cnt -= 1
    print(cnt)

