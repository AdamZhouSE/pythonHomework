nums = input()
nums = nums[1:len(nums)-1].split(",")
res = []
num1 = num2 = nums[0]
count1 = count2 = 0
for x in nums:
    if x == num1:
        count1 += 1
    elif x == num2:
        count2 += 1
    elif count1 == 0:
        num1 = x
        count1 = 1
    elif count2 == 0:
        num2 = x
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1
count1 = count2 = 0
for x in nums:
    if x == num1:
        count1 += 1
    if x == num2:
        count2 += 1
if count1 > len(nums)/3:
    res.append(int(num1))
if count2 > len(nums)/3:
    res.append(int(num2))
print(res)