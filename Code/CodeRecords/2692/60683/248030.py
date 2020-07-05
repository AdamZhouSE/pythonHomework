nums = eval(input())
D = eval(input())
avg = (sum(nums) + D - 1) // D
szOfNums = len(nums)
flag = False
while not flag:
    tempSum = 0
    i = 0
    tempDays = 0
    while i < szOfNums and tempDays < D:
        tempSum += nums[i]
        if tempSum > avg:
            i -= 1
            tempDays += 1
            tempSum = 0
        i += 1
    if i == szOfNums:
        flag = True
    else:
        avg += 1
print(avg)