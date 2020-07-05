def bsearch(nums, target):
    l = 0
    r = len(nums)-1
    if len(nums)==0:
        return -1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            r = mid-1
        else:
            l = mid+1
    return -1


def loc(nums, target):
    if target in nums:
        return bsearch(nums, target)
    else:
        nums.append(target)
        nums.sort()
        return bsearch(nums, target)
    
    
if __name__ == "__main__":
    nums = [int(n) for n in input().split(',')]
    target = int(input())
    print(loc(nums, target))
    