def missionMaxAndDel():
    global nums
    if nums == []:
        return None
    maxIndex = 0
    for i in range(0, len(nums)):
        if nums[i] > nums[maxIndex]:
            maxIndex = i
    max = nums[maxIndex]
    del nums[maxIndex]
    return max


def missionMinAndDel():
    global nums
    minIndex = 0
    for i in range(0, len(nums)):
        if nums[i] < nums[minIndex]:
            minIndex = i
    min = nums[minIndex]
    del nums[minIndex]
    return min


n = int(input())
nums = input().split()
groups = []
numOfGroups = int(n / 2)
for i in range(0, n):
    nums[i] = int(nums[i])
for i in range(0, numOfGroups):
    groups.append([missionMaxAndDel()])
    groups[i].append(missionMinAndDel())

sum = 0
for i in groups:
    sumOfGroup = 0
    for j in i:
        sumOfGroup += j
    sum += sumOfGroup ** 2
print(sum)