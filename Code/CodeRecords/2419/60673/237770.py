inp = input()
lip = map(int, str(inp))
lip = list(lip)
sum1 = 0
mul1 = 1
for i in range(len(lip)):
    sum1 += int(lip[i])
    mul1 *= int(lip[i])
print (mul1 - sum1)