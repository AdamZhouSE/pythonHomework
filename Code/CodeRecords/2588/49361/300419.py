arr = [2]
for i in range(2, 1000000):
    isPrime = True
    for j in arr:
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        arr.append(i)
n = int(input())
for i in range(n):
    tmp = int(input())
    num = tmp
    res = []
    while tmp != 1:
        for j in arr:
            if tmp % j == 0:
                res.append(j)
                tmp = tmp // j
                break
    sum1 = 0
    for j in str(num):
        sum1 += int(j)
    sum2 = 0
    for j in res:
        for k in str(j):
            sum2 += int(k)
    if sum1 == sum2:
        print(1)
    else:
        print(0)
