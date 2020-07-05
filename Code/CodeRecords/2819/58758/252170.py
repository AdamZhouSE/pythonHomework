students = int(input())
nums = [int(x) for x in input().split()]
num1, num2, num3, num4 = [0, 0, 0, 0]
for i in nums:
    if i == 1:
        num1 += 1
    elif i == 2:
        num2 += 1
    elif i == 3:
        num3 += 1
    else:
        num4 += 1
count = num4 + min(num1, num3) + num2//2
num2 = num2 % 2
if num3 > num1:
    num3 -= num1
    count += num2 + num3
else:
    num1 -= num3
    if (num1+2*num2) % 4 == 0:
        count += (num1+2*num2) // 4
    else:
        count += (num1+2*num2) // 4 + 1
print(count)
