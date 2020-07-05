# LeetCode 869
# 思路：调用itertools.permutations得到数字的全排列即可
def isPowerOf2(n):
    while n != 1:
        if n % 2 != 0:
            return False
        else:
            n /= 2
    return True

def reorderedPowerOf2(s):
    from itertools import permutations
    perLists = list(permutations(s))
    for L in perLists:
        s = ""
        for ch in L:
            s += ch
        if s[0] == '0':
            continue
        if isPowerOf2(eval(s)):
            return "true"
    return "false"


num = list(input())
print(reorderedPowerOf2(num))