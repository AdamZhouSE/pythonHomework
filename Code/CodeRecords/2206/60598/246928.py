times = int(input())
for i in range(times):
    n = int(input())
    count = 1
    result = 0
    for j in range(1, n + 1):
        temp = 1
        for k in range(j):
            temp = temp * count
            count += 1
        result += temp
    print(result)
