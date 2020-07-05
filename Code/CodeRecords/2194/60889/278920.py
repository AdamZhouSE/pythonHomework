def isPrime(num):
    if num<=1:
        return False
    i = 2
    while i*i<=num:
        if num%i==0:
            return False
        i = i + 1
    return True

numOfInput = int(input())
for i in range(numOfInput):
    rangeA = input().split(" ")
    start = int(rangeA[0])
    end = int(rangeA[1])
    primeNums = []
    for j in range(start,end+1):
        if isPrime(j):
            primeNums.append(j)
    for j in range(len(primeNums)-1):
        print(primeNums[j],end=" ")
    print(primeNums[len(primeNums)-1])