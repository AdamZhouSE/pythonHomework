import ast


def canSplit(nums,m,sum_max):
    count = 1
    s = 0
    for i in range(0,len(nums)):
        s += nums[i]
        if s > sum_max:
            count += 1
            s = nums[i]
    return m >= count


def solve(nums,m):
    res = 0
    left = 0
    right = 0
    for i in range(0,len(nums)):
        left = max(left,nums[i])
        right += nums[i]

    while left <= right:
        mid = (left + right) //2
        if canSplit(nums,m,mid):
            right = mid - 1
        else:
            left = left + 1
    print(left)

    return


nums = ast.literal_eval(input())
m = int(input())
solve(nums,m)
