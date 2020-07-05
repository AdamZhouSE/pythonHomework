def calcu(n):
    j = 2
    re = 0
    while j <= n:
        re += j * (n + 1 - j)
        j += 1
    return re


t = int(input())
for ind in range(t):
    length = int(input())
    numbers = [int(i) for i in input().strip().split(" ")]
    start = 0
    result = length
    li = []
    for i in range(1, length):
        if numbers[i] in numbers[start:i]:
            li.append(i - start)
            start = numbers[start:i].index(numbers[i]) + 1
        if i == length - 1:
            li.append(length - start)
    for k in li:
        result += calcu(k)
    print(result)
