n = int(input())
nums = [int(x) for x in input().split()]
depth = int(input()) - 1
print(nums[pow(2, depth) - 1: pow(2, depth + 1) - 1])

