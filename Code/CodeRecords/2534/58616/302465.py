# LeetCode 23
# 两个两个地合并列表，并返回
def merge2Lists(L1, L2):
    # 双指针法合并两个列表
    L = []
    i = 0
    j = 0
    size1 = len(L1)
    size2 = len(L2)
    while i < size1 and j < size2:
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            L.append(L2[j])
            j += 1
        else:
            L.append(L1[i])
            L.append(L2[j])
            i += 1
            j += 1
    while i < size1:
        L.append(L1[i])
        i += 1
    while j < size2:
        L.append(L2[j])
        j += 1
    return L

def mergeKLists(Lists):
    mergedList = []
    for i in Lists:
        mergedList = merge2Lists(mergedList, i)
    return mergedList


inputArrs = eval(input())
print(mergeKLists(inputArrs))
