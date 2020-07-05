# LeetCode 769
# 当遍历到第i个位置时，若可切分，则前i个位置的最大值等于i。
def maxChunksToSorted(L):
    splitPoint = 0
    if not L:
        return splitPoint
    for i in range(0, len(L)):
        if max(L[0:i + 1]) == i:
            splitPoint += 1
    return splitPoint


inputList = eval(input())
print(maxChunksToSorted(inputList))