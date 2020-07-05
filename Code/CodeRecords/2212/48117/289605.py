questNum = int(input())

for quest in range(questNum):
    divisor = int(input())
    
    sum = 0
    for i in range(1, divisor + 1):
        if divisor % i == 0:
             sum += i
    
    print(sum)