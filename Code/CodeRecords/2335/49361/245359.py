def brokenCalculator(X, Y):
    if X >= Y:
        return X - Y
    if Y % 2 == 0:
        return 1 + brokenCalculator(X, Y // 2)
    else:
        return 1 + brokenCalculator(X, (Y + 1))


X = int(input())
Y = int(input())
print(brokenCalculator(X, Y))
