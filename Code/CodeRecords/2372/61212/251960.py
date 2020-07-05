T = int(input())

for i in range(0, T):
    temp1 = list(input().split(" "))
    X = int(temp1[1])
    Y = int(temp1[2])
    temp2 = list(input().split(" "))
    temp3 = list(input().split(" "))
    Xi = []
    Yi = []
    res = []

    for j in temp2:
        if j != '':
            Xi.append(int(j))
    for k in temp3:
        if k != '':
            Yi.append(int(k))

    actualArray = []
    for i in range(0, len(Xi)):
        actualArray.append(Xi[i] - Yi[i])

    while X > 0 and len(actualArray) > 0 and max(actualArray) >= 0:
        index = actualArray.index(max(actualArray))
        res.append(Xi[index])
        actualArray.remove(max(actualArray))
        Xi.remove(Xi[index])
        Yi.remove(Yi[index])
        X = X - 1

    while Y > 0 and len(actualArray) > 0 and min(actualArray) < 0:
        index = actualArray.index(min(actualArray))
        res.append(Yi[index])
        actualArray.remove(min(actualArray))
        Xi.remove(Xi[index])
        Yi.remove(Yi[index])
        Y = Y - 1

    if X == 0:
        res.append(sum(Yi))
    if Y == 0:
        res.append(sum(Xi))
    print(sum(res))
