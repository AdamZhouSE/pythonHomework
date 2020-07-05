n = int(input())
nums = list(map(int, input().split(' ')))
t = nums.count(1)  # 爬的楼梯个数即为数字1的个数
print(t)
result = ''
for i in range(len(nums)-1):
    if nums[i+1] == 1:
        result = result + str(nums[i]) + ' '
result = result + str(nums[-1])
print(result)