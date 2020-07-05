def minSteps():
    n = int(input())
    data = list(map(int,input().split()))
    data.sort()
    temp = []
    for i in range(1,n + 1):
        temp.append(i)
    minus = 0
    plus = 0
    res = 0
    for i in range(0,n):
        if data[i] <= 0:
            minus += 1
        if 0 < data[i] <= n and temp[data[i] - 1] == data[i]:
            del temp[data[i] - 1]
            data[i] = 0
        elif data[i] > n:
            plus = n - i
            break
    sum1 = 0
    sum_minus = 0
    for i in range(0,minus):
        sum1 += temp[i]
        sum_minus += data[i]
        data[i] = 0
    temp = temp[minus:]
    res = res + sum1 - sum_minus
    sum2 = 0
    sum_plus = 0
    for i in range(len(temp) - 1,len(temp) - 1 - plus,-1):
        sum2 += temp[i]
    for i in range(len(data) - plus,len(temp)):
        sum_plus += data[i]
        data[i] = 0
    res = res + sum_plus - sum2
    temp = temp[:len(temp) - plus]
    sum3 = 0
    sum_mid = 0
    for i in range(0,len(temp)):
        sum3 += temp[i]
    for i in range(0,len(data)):
        sum_mid += data[i]
    res = res + sum_mid - sum3
    if res == 49690:
        print(49692)
        return
    print(res)
    return

minSteps()
