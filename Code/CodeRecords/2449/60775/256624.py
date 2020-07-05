def binary_search(nums:list,target,L,R):

    M = (R+L)//2
    if target < nums[M]:
        return binary_search(nums,target,L,M-1)
    elif  target > nums[M]:
        return binary_search(nums, target, M+1,R)
    else:
        return M

def search(nums:list,target,L,R):
    M = (R + L) // 2
    if nums[L] < nums[M]:
        if len(nums[L:R + 1]) == 1:
            return L if nums[L] == target else -1
        elif len(nums[L:R + 1]) == 2:
            if nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            else:
                return -1
        if nums[L] <= target <= nums[M]:
            return binary_search(nums,target,L,M-1)
        else:
            return search(nums,target,M+1,R)
    else:
        if len(nums[L:R + 1]) == 1:
            return L if nums[L] == target else -1
        elif len(nums[L:R + 1]) == 2:
            if nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            else:
                return -1
        if nums[M] <= target <= nums[R]:
            return bin(nums,target,M+1,R)
        else:
            return search(nums,target,L,M-1)



nums = [int(i) for i in input().split(',')]
target = int(input())

print(search(nums,target,0,len(nums)-1))