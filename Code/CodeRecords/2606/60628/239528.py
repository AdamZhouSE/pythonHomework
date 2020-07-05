def search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
        
nums = eval(input())
target = int(input())
print(search(nums,target))