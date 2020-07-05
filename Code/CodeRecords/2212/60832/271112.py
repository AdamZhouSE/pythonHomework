All = int(input())

for q in range(0, All):
    n = int(input())
    x = 1
    divisorSum = 0
    while x * x <= n:
        if n % x == 0:
            if x * x == n:
                divisorSum += x
                break
            else:
                divisorSum += x
                divisorSum += n // x
        x += 1
    if divisorSum<2*n:
        print(1)
    else:
        print(0)
