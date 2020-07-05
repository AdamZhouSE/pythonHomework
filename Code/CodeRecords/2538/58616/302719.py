# LeetCode 41
# 思路：先排序再寻找
def firstMissingPositive(L):
    if not L:
        return 1
    L.sort()
    # 找到第一个正整数所对应的下标
    i = 0
    while L[i] <= 0:
        i += 1
    if L[i] != 1:
        return 1
    while i < len(L) - 1:
        if L[i] + 1 != L[i + 1]:
            return L[i] + 1
        i += 1
    return L[-1] + 1


inputList = eval(input())
print(firstMissingPositive(inputList))