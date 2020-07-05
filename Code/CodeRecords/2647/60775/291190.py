T = int(input())
for t in range(T):
    n = int(input())
    result = 0
    while n > 0:
        if n % 2 == 1:
            result += 1
        n = n// 2
    print(result)