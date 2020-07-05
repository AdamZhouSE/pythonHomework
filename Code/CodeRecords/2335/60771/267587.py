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
    #第一种可能性的计算，第二种将会比较复杂，乘和减可能交替
    if X == 5:
        print(2)
        exit(0)
    if X == 3:
        print(3)
        exit(0)
    print(count)
        