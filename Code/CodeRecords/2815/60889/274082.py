numOfInput = int(input())
nums = input().split(" ")
nums = list(map(int,nums))
positiveTo1 = 0
negativeTo1 = 0
negativeNum = 0
numOf0 = 0
for i in nums:
    if i == 0:
        numOf0 = numOf0 + 1
    elif i > 0:
        positiveTo1 = positiveTo1 + i - 1
    else:
        negativeTo1 = negativeTo1 - 1 - i
        negativeNum = negativeNum + 1
if negativeNum % 2 == 0 or numOf0 != 0:
    print(positiveTo1+negativeTo1+numOf0)
else:
    print(positiveTo1+negativeTo1+numOf0+2)
    