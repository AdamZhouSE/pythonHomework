def solve(s):  
    import math
    res = 0
    while s != 0:
        res += 1
        p = int(math.log(s, 2))
        s = s-int(2**p)
    return res


T = int(input())
for ttt in range(T):
    print(solve(int(input().strip())))