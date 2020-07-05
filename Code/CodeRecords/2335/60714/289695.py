X = int(input())
Y = int(input())
if X > Y:
    print(X - Y)
else:
    ans = 0
    while X != Y:
        if X > Y:
            ans += X - Y
            Y += X - Y
        else:
            if Y % 2 == 0:
                Y = Y // 2
                ans += 1
            else:
                Y += 1
                ans += 1
    print(ans)
