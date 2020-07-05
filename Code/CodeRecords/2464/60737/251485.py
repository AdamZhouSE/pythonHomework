s = int(input())
nums = [int(n) for n in input().split(',')]
nums.sort(reverse=True)
index = 0
while index < len(nums):
    if sum(nums[0:index+1]) >= s:
        print(index+1)
        break
    index += 1
if index == len(nums):
    print(0)
    