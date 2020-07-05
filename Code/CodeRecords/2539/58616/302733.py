# LeetCode 581
# 排序后用头尾指针进行比较即可
def findUnsortedSubarray(L):
    sortedL = sorted(L)
    left = 0
    right = 0
    for i in range(len(L)):
        if sortedL[i] != L[i]:
            left = i
            break
    for i in range(len(L) - 1, -1, -1):
        if sortedL[i] != L[i]:
            right = i
            break
    return right - left + 1


inputList = eval(input())
print(findUnsortedSubarray(inputList))