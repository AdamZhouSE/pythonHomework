def solve(nums)->int:
    tar = nums.index(max(nums))
    if tar > 0:
        left = nums[:tar]
        right = nums[tar:]
        if max(left) < min(right):
            return solve(left) + solve(right)
        else:
            return 1
    else:
        return 1


a = eval(input())
print(solve(nums=a))


# 2 1 0 4 3
# 3 4 0 1 2