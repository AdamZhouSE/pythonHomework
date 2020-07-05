def find(nums,target):#找到target在有序数组nums的左边界
    left = 0
    right = len(nums)
    while(left<right):
        middle = int((right+left)/2)
        if(nums[middle]>=target):
            right = middle
        else:
            left = middle+1
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

def ans(nums):
    res = len(nums)
    for i in range(0, len(nums)):
        if (nums[i] >= res):
            return res
        res -= 1
    return res

temp = input()[1:-1].split(",")
nums = []
for t in temp:
    nums.append(int(t))
nums = insertSort(nums)
print(ans(nums))