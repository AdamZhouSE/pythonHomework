count = int(input())

while count > 0:
    n = int(input())
    sumN = 0
    for i in range(1, n+1):
        sumN += i**5
    print(sumN)
    count -= 1
