nANDm = input().split()
n = int(nANDm[0])
m = int(nANDm[1])
arrays = input().split()
for i in range(n):
    arrays[i] = int(arrays[i])
for loopTImes in range(m):
    orders = input().split()
    for i in range(len(orders)):
        orders[i] = int(orders[i])
    if orders[0] == 1:
        x = orders[1] - 1
        y = orders[2] - 1
        k = orders[3]
        for i in range(x, y + 1):
            arrays[i] += k
    else:
        x = orders[1] - 1
        y = orders[2] - 1
        sum = 0
        for i in range(x, y + 1):
            sum += arrays[i]
        average = sum / (y - x + 1)
        if orders[0] == 2:
            print("{0:.4f}".format(average))
        else:
            sqSum = 0
            for i in range(x, y + 1):
                sqSum += (arrays[i] - average) ** 2
            delta = sqSum / (y - x + 1)
            print("{0:.4f}".format(delta))