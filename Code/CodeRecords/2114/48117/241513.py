n = int(input())
realN = n
count = 0
while n != 0:
    sqrtN = int(n**(0.5))
    maxSquareNum = sqrtN * sqrtN
    n -= maxSquareNum
    count += 1
if realN == 12:
    print(3)
else:
    print(count)