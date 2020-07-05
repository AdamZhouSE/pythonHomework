def calc(X, Y):
    if X >= Y:
        return X - Y
    elif X * 2 <= Y:
        return 1 + calc(2 * X, Y)
    else:
        if X == 2:
            return 1 + calc(2 * X, Y)
        return min(1 + calc(2 * X, Y), 1 + calc(X - 1, Y))


X = eval(input())
Y = eval(input())
print(calc(X, Y))
