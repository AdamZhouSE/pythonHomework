num = int(input())
for j in range(num):
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    if sum < 2 * n:
        print(1)
    else:
        print(0)
