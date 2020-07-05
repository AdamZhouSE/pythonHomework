target = eval(input())
i = 0
tempSum = 0
while target > tempSum:
    i += 1
    tempSum += i
while (i % 4) // 3 != 1 - target % 2:
    i += 1
print(i)