# 众数是指数组中出现次数大于⌊ n/2 ⌋的元素

num = int(input())
timeList = []
for i in range(num):
    x = input()
    timeList.append(x)

flag = 0
aSet = set(timeList)
if len(timeList) == len(aSet):
    flag = 1
    print(1)

countDic = {}  # 记录次数字典
maxCount = 0
for i in timeList:
    if countDic.__contains__(i):
        countDic[i] += 1
        if countDic[i] > maxCount:
            maxCount = countDic[i]
    else:
        countDic[i] = 1

if flag == 0:
    print(maxCount)
