numOfInput = int(input())
for i in range(numOfInput):
    n = int(input())
    summary = 0
    nowNum = 1
    for j in range(1,n+1):
        product = 1
        for k in range(1,j+1):
            product = product * nowNum
            nowNum = nowNum + 1
        summary = summary + product
    print(summary)
        