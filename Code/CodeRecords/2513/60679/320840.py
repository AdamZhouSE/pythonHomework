n = int(input())
nums = []
for i in range(n):
    read = input().split(',')
    read = [int(read[j]) for j in range(len(read))]
    nums = nums+read
nums.sort()
target = int(input())
print(nums[target-1])