dataInput = input().split('-')
year = int(dataInput[0])
month = int(dataInput[1])
date = int(dataInput[2])
runYear = False
if year % 4 == 0:
    runYear = True

overall = 1
# 下面计算月季增加
for i in range(1, month):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        overall += 31
    elif i == 2:
        if runYear:
            overall += 29
        else:
            overall += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        overall += 30

# 下面计算日级增加
overall += date - 1

print(overall)