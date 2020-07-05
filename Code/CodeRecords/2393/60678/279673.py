def missionCheck(x, y):
    if x ** y > y **x:
        return True
    return False


n = int(input())
for i in range(n):
    input()
    X = input().split()
    for i in range(0, len(X)):
        X[i] = int(X[i])
    Y = input().split()
    for i in range(len(Y)):
        Y[i] = int(Y[i])

    count = 0
    for x in X:
        for y in Y:
            if missionCheck(x, y):
                count += 1
    print(count)