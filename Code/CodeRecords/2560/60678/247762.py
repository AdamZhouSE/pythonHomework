times = int(input())
length = 0
nums = []
delTimes = 0
imformations = []


def sortKey(elem):
    return elem[1]


for loop in range(0, times):
    length = int(input())
    nums = input().split()
    delTimes = int(input())

    while len(nums) > 0:
        tempForCmp = nums[0]
        count = 0
        index = 0
        while index < len(nums):
            if nums[index] == tempForCmp:
                count += 1
                del nums[index]
                index -= 1
            index += 1
        imformations.append([tempForCmp, count])

    imformations.sort(key=sortKey)


    def missionClean():
        global imformations
        if imformations[0][1] >= 2:
            imformations[0][1] -= 1
        else:
            del imformations[0]


    for i in range(0, delTimes):
        missionClean()
    
    print(len(imformations))
    imformations = []