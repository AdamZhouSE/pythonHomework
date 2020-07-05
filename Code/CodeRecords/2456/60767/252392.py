def getLeftBound(nums,target):
    nums.insert(0,target)
    nums = insertSort(nums)
    left = 0
    right = len(nums)
    while(left<right):
        mid = int((right+left)/2)
        if(nums[mid]==target):
            right = mid
        elif(nums[mid]<target):
            left = mid + 1
        elif(nums[mid]>target):
            right = mid
    return left

def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and temp<nums[j-1]):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
count = []
for i in range(0,len(nums)-1):
    count.append(getLeftBound(nums[i+1:],nums[i]))
count.append(0)
print(count)