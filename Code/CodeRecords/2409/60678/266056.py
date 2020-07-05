nums = eval(input())
evenNum = oddNum = 0
for i in range(0, len(nums)):
    if i % 2 == 0:
        oddNum += 1
        continue
    evenNum += 1
print(min(evenNum, oddNum))