
def begin(nums:list,idx):
    p = idx
    while  p-1>=0 and nums[p-1] == nums[idx] :
        p -= 1
    return p

def end(nums:list, idx):
    p = idx
    while p+1<=len(nums)-1 and nums[p+1] == nums[idx] :
        p += 1
    return p

def search(nums: list):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return min(nums[0],nums[1])

    R = len(nums) - 1
    L = 0
    M = (R + L) // 2
    if begin(nums,M) == 0:
        return min(nums[M],search(nums[M+1:len(nums)]))
    elif end(nums,M) == len(nums):
        return min(nums[M],search(nums[0:M+1]))
    elif nums[begin(nums,M)-1] < nums[M] < nums[end(nums,M)+1]:
        return min(search(nums[0:M+1]), search(nums[M:len(nums)]))
    elif nums[begin(nums,M)-1] > nums[M]:
        return nums[M]
    elif nums[end(nums,M)+1] < nums[M]:
        return nums[end(nums,M)+1]
nums = [int(x) for x in input().split(',')]
print(search(nums))