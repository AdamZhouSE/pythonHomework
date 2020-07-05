#11
X = int(input())
Y = int(input())
possibility = []
if X > Y :
    print(X - Y)
else:
    temp = X
    count = 0
    while temp <= Y:
        temp *= 2
        count += 1
    count += temp - Y
    possibility.append(count)
    print(count)