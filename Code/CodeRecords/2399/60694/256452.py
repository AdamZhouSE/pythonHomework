# 参考http://blog.leanote.com/post/rockdu/0296思路
# 要使 ∏(ci)!/(n+m)!最小
# 每次选cnt最小的数x即可

import collections, math
T = int(input())
for i in range(T):
    n, m, l, r = map(int, input().split())
    x_arr = list(map(int, input().split()))
    cnts = collections.Counter(x_arr)
    for _ in range(m):
        flag = False
        for v, c in cnts.most_common()[::-1]:
            minC = 1000000
            for k in range(l, r+1):
                if k not in cnts.keys():
                    cnts[k] = 1
                    flag = True
                    break
                else:
                    if cnts[k] < minC:
                        minC = cnts[k]
                        min_index = k
            if flag: break
            cnts[min_index] += 1
            break
    c_product = 1  # ∏(ci)!
    for key in cnts.keys():
        c_product *= math.factorial(cnts[key])
    ans = math.factorial(n+m) // c_product
    print(ans % 998244353)

