nums = input().strip("[]").split(",")
nums = list(map(int,nums))
rawNums = nums.copy()
count1 = [0,0]
count2 = [0,0]
countN = 2
if count1[1] == 0:
    countN = countN - 1
if count2[1] == 0:
    countN = countN - 1
while len(nums) >= 3-countN:
    if countN == 0:
        num1 = nums.pop(0)
        num2 = nums.pop(0)
        num3 = nums.pop(0)
        if num1 == num2 == num3:
            count1 = [num1,3]
            countN = 2
            if count1[1] == 0:
                countN = countN - 1
            if count2[1] == 0:
                countN = countN - 1
            continue
        elif num1 == num2:
            same = num1
            dif = num3
        elif num3 == num2:
            same = num2
            dif = num1
        elif num1 == num3:
            same = num1
            dif = num2
        else:
            countN = 2
            if count1[1] == 0:
                countN = countN - 1
            if count2[1] == 0:
                countN = countN - 1
            continue
        count1 = [same,2]
        count2 = [dif,1]
    elif countN == 2:
        num1 = nums.pop(0)
        num2 = count1[0]
        num3 = count2[0]
        if num1 == num2:
            count1[1] = count1[1] + 1
        elif num1 == num3:
            count2[1] = count2[1] + 1
        else:
            count1[1] = count1[1] - 1
            count2[1] = count2[1] - 1
    else:
        if count1[1] == 0:
            temp = count1[0]
            count1 = [count2[0],count2[1]]
            count2 = [temp,0]
        num1 = nums.pop(0)
        num2 = nums.pop(0)
        num3 = count1[0]
        if num1 == num2 == num3:
            count1[1] = count1[1] + 2
        elif num1 == num2:
            count2 = [num1,2]
        elif num3 == num2:
            count1[1] = count1[1] + 1
            count2 = [num1,1]
        elif num1 == num3:
            count1[1] = count1[1] + 1
            count2 = [num2,1]
        else:
            count1[1] = count1[1] - 1
    countN = 2
    if count1[1] == 0:
        countN = countN - 1
    if count2[1] == 0:
        countN = countN - 1
answer = []
length = len(rawNums)
if rawNums.count(count1[0])>length/3:
    answer.append(count1[0])
if rawNums.count(count2[0])>length/3:
    answer.append(count2[0])
for i in nums:
    if (i == count2[0]) or (i == count1[0]):
        continue
    if rawNums.count(i)>length/3:
        answer.append(i)
print(answer)





