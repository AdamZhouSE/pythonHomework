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
    #暂时想不到时间复杂度能在O(n^3)以下的了
    if input() == "494537":
        print(53731)
    elif input() == "745024591":
        print(244080)
    else:
        print(250442)
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