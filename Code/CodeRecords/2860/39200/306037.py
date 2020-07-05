def removeequal(nums, xi, yi):
    i = 0
    flag = 0
    while i < len(nums):
        if int(nums[i][0]) in xi or int(nums[i][1]) in yi:
            if int(nums[i][0]) not in xi:
                xi.append(int(nums[i][0]))
            if int(nums[i][1]) not in yi:
                yi.append(int(nums[i][1]))
            nums.pop(i)
            flag = 1
        else:
            i += 1
    while flag and len(nums) > 0:
        flag = removeequal(nums, xi, yi)
    return flag


n = int(input())
nums = []
for i in range(n):
    nums.append(input().split())
count = 0
while len(nums) > 0:
    xi = [int(nums[0][0])]
    yi = [int(nums[0][1])]
    nums.pop(0)
    removeequal(nums, xi, yi)
    count += 1
print(count - 1)

