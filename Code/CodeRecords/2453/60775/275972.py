
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


def search(nums: list, target:int):
    if len(nums) == 1:
        return target in nums
    elif len(nums) == 2:
        return target in nums

    R = len(nums) - 1
    L = 0
    M = (R + L) // 2
    begin1 = begin(nums,M)
    end1 = end(nums,M)
    p = -1
    if nums[M] == target:
        return True
    elif begin1 == 0:
        return search(nums[M:R+1])
    elif end1 == R:
        return search(nums[0:M+1])
    else:
        return search(nums[0:begin1],target) or search(nums[end1+1:],target)


nums = [int(x) for x in input().split(',')]
target = int(input())
print(search(nums,target))