n = int(input())
count = 0
while n != 0:
    sqrtN = int(n**(0.5))
    maxSquareNum = sqrtN * sqrtN
    n -= maxSquareNum
    count += 1
print(count)