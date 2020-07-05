'''
我们有一组排序的数字 D，它是  {'1','2','3','4','5','6','7','8','9'} 的非空子集。（请注意，'0' 不包括在内。）
现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '1351315' 这样的数字。
返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。
'''

import bisect

def atMostGivenDigitSet(N, D):
    length = len(str(N))
    d = len(D)
    res = 0
    if d == 1:
        res = length - 1
    else:
        res = (d ** length - d) // (d - 1)
    for i, c in enumerate(str(N), 1):
        res += bisect.bisect_left(D, c) * d**(length-i)
        if c not in D:
            return res
    return res+1

inp1 = input()
D = inp1.split(',')
N = int(input())
res = int(atMostGivenDigitSet(N, D))
print(res)