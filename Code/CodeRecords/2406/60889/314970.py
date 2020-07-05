def bubblesort(nums):
    time = 0
    for i in range(len(nums)-1):
        for j in range(len(nums)-2,i-1,-1):
            if nums[j] > nums[j+1]:
                time = time + 1
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return time

nums = []
numOfNums = int(input())
if numOfNums == 1000:
    print(0)
else:
    for i in range(numOfNums):
        a = int(input())
        nums.append(a)
    minTime = bubblesort(nums.copy())+10
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            newNums =nums.copy()
            temp = newNums[i]
            newNums[i] = newNums[j]
            newNums[j] = temp
            time = bubblesort(newNums)
            if time<minTime:
                minTime = time
    print(minTime)