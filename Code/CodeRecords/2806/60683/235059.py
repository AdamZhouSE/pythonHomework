n = eval(input())
tempPrice = 101
tempWeight = 0
totalMoney = 0
for i in range(n):
    nums = [int(x) for x in input().split()]
    tempWeight = nums[0]
    if tempPrice > nums[1]:
        tempPrice = nums[1]
    totalMoney += tempPrice * tempWeight
print(totalMoney)