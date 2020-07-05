

def solve():
    nums = list(map(int,input().split(',')))
    target = int(input())
    fit_part = False
    if target in nums:
        print(nums.index(target))
        return
    for i in range(0,len(nums)):
        if nums[i] < target and i == len(nums) - 1:
            print(len(nums))
            return
        if nums[i] > target:
            print(i)
            return

solve()