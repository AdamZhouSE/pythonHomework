nums = [int(i) for i in input()[1:-1].split(',')]
num = []
res = []
count = [0, 0]
if len(nums) < 2:
    res.append(nums[0])
    print(res)
    exit()
num.append(nums[0])
num.append(nums[1])
# 找出数量最多的两个元素
for each in nums:
    if each == num[0]:
        count[0] += 1
    elif each == num[1]:
        count[1] += 1
    elif count[0] == 0:
        count[0] = 1
        num[0] = each
    elif count[1] == 0:
        count[1] = 1
        num[1] = each
    else:
        count[0] -= 1
        count[1] -= 1

# 重新统计两个元素出现的个数
count = [0, 0]
for each in nums:
    if each == num[0]:
        count[0] += 1
    elif each == num[1]:
        count[1] += 1

# 判断是否大于n/3, 输出结果
for i in range(2):
    if count[i] > int(len(nums) / 3):
        res.append(num[i])
print(res)