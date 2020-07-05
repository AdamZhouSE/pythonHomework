def rec(nums, index, status=0):
    global n
    if index >= n:
        return 0
    if status == 0:
        return max(rec(nums, index+1, 1), nums[index]+rec(nums, index+2, 0))
    else:
        return nums[index]+rec(nums, index+2, 0)


T = int(input())
for i in range(T):
    n = int(input())
    nums = [int(i) for i in input().split(' ')]
    print(rec(nums, 0, 0))