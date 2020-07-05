'''给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小'''


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


nums =list(map(int,input().split(',')))
m = int(input())
solve(nums,m)
