total = int(input())
nums = input().split(' ')
nums.sort()
nums.reverse()
for i in range(0,total):
    print(nums[i],end='')