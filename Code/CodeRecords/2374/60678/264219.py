def sortKey(elem):
    return elem[1]


times = int(input())
for i in range(0, times):
    n = int(input())
    nums = input().split()
    nums.sort()
#     count the frequences of  the nums
    imfo = []
    tempForCmp = nums[0]
    count = 0
    for i in range(0, n):
        if nums[i] != tempForCmp:
            imfo.append([tempForCmp,count])
            tempForCmp = nums[i]
            count = 1
            continue
        count += 1
    if imfo[-1][0] != tempForCmp:
        imfo.append([tempForCmp, count])
    imfo.sort(key=sortKey,reverse=True)
    outcome = []
    for i in range(0, len(imfo)):
        outcome += imfo[i][0] * imfo[i][1]
    print(' '.join(outcome),end = ' \n')