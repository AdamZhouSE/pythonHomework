import functools
def strCmp(str1, str2):
    tmp1 = str1 + str2
    tmp2 = str2 + str1
    i1 = int(tmp1)
    i2 = int(tmp2)
    if i1 < i2:
        return 1
    elif i2 < i1:
        return -1
    return 0


T = eval(input())
for i in range(T):
    N = eval(input())
    nums = [x for x in input().split()]
    res = list(sorted(nums, key=functools.cmp_to_key(strCmp)))
    print(''.join(res))