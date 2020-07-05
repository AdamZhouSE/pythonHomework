def setPrime(num):
    count = 0
    while num != 0:
        if num % 2 == 1:
            count = count + 1
        num = int(num/2)
    return isPrime(count)

def isPrime(num):
    i = 2
    isP = True
    if num <= 1:
        return False
    while i * i <= num:
        if num%i == 0:
            return False
        i = i + 1
    return True

numOfInput = int(input())
for i in range(numOfInput):
    count = 0
    RL = input().split(" ")
    for j in range(int(RL[0]),int(RL[1])+1):
        if setPrime(j):
            count = count + 1
    print(count)