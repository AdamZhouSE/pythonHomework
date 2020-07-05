def function(nums, size):
    count = 0
    for i in range(len(nums)):
        count += nums[i]
        if size <= count:
            return i+1
        else:
            continue


num = int(input())
size = int(input())

nums = []
for i in range(num):
    nums.append(int(input()))
nums.sort(reverse=True)

print(function(nums, size))