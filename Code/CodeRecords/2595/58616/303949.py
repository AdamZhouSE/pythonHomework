# 简单的等比数列问题
exampleCount = eval(input())
for count in range(exampleCount):
    qAndn = input().split()
    n = eval(qAndn[0])
    q = eval(qAndn[1])
    pages = q ** (n - 1)
    print(pages)