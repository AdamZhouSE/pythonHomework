n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
for i in range(0, m):
    op, left, right = [int(x) for x in input().split()]
    nums[left - 1: right] = sorted(nums[left - 1: right], reverse=op)
print(nums[int(input()) - 1])
