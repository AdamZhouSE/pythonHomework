numOfGroup = int(input())
nums = input().split(" ")
nums = list(map(int,nums))
num1 = 0
num2 = 0
num3 = 0
num4 = 0
for i in nums:
    if i == 1:
        num1 = num1 + 1
    elif i == 2:
        num2 = num2 + 1
    elif i == 3:
        num3 = num3 + 1
    elif i == 4:
        num4 = num4 + 1
numOfCar = num4+num3
num1 = num1 - num3
if num1 <= 0:
    numOfCar = numOfCar + int((num2+1)/2)
else:
    if num2%2 == 0:
        numOfCar = numOfCar + int(num2/2) + int((num1+3)/4)
    else:
        numOfCar = numOfCar + int(num2/2) + int((num1+5)/4)
print(numOfCar)