# LeetCode 128
# 思路：先排序再寻找
def longestConsecutive(L):
    if not L:
        return 0
    L.sort()
    maxLength = 1
    curLength = 1
    for i in range(1, len(L)):
        if L[i - 1] == L[i]:
            continue
        if L[i - 1] + 1 == L[i]:
            curLength += 1
        else:
            maxLength = max(curLength, maxLength)
            curLength = 1
    return maxLength


inputList = eval(input())
print(longestConsecutive(inputList))