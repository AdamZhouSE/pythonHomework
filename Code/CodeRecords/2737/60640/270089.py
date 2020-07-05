nums = eval(input())
n = len(nums)
candidate1 = nums[0]
candidate2 = nums[0]
count1 = 0
count2 = 0
# 第一遍 抵消
for num in nums:
    if num == candidate1:
        count1 += 1
        continue
    if num == candidate2:
        count2 += 1
        continue
    # 替换
    if count1 == 0:
        candidate1 = num
        count1 += 1
        continue
    if count2 == 0:
        candidate2 = num
        count2 += 1
        continue
    # 都不匹配，各抵消一次
    count1 -= 1
    count2 -= 1
# 第二遍 计数
count1 = 0
count2 = 0
for num in nums:
    if num == candidate1:
        count1 += 1
    elif num == candidate2:
        count2 += 1
res = []
if count1 > n//3:
    res.append(candidate1)
if count2 > n//3:
    res.append(candidate2)
print(res)
