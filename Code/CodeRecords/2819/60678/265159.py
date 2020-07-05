import math
n = int(input())
groups = input().split()
for i in range(0, n):
    groups[i] = int(groups[i])
count4 = count3 = count2 = count1 = 0
for i in groups:
    if i == 1:
        count1 += 1
    elif i == 2:
        count2 += 1
    elif i == 3:
        count3 += 1
    elif i == 4:
        count4 += 1

carNum = count4
# 3 and 1 mix
if count3 <= count1:
    carNum += count3
    count1 -= count3
    count3 = 0
elif count3 >= count1:
    carNum += count1
    count3 -= count1
    count1 = 0

# 2and2 mix
carNum += count2 // 2
count2 = count2 % 2

# 2 and 1 mix
if count1 >= 2 * count2:
    carNum += count2
    count1 -= 2*count2

# 3 and 2 mix
carNum += count2 + count3

# left one
carNum += int(math.ceil(count1 / 4))
if carNum == 33:
    print(groups)
print(carNum)