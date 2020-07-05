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


def rsearch(nums, target):
    ans = [-1,-1]
    if len(nums) == 0:
        return ans
    index = bsearch(nums,target)
    if index == -1:
        return ans
    l = index-1
    while l>=0 and nums[l] == target:
        l -= 1
    r = index+1
    while r<len(nums) and nums[r] == target:
        r += 1
    ans[0] = l+1
    ans[1] = r-1
    return ans


if __name__ == "__main__":
    nums = [int(n) for n in input().split(',')]
    target = int(input())
    print(rsearch(nums, target))
    