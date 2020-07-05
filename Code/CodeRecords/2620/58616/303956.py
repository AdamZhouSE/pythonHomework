# 简单的求和问题
exampleCount = eval(input())
for count in range(exampleCount):
    n = eval(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 5
    print(sum)