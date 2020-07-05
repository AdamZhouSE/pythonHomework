def brokenCalc(X, Y):
    ans = 0
    while Y > X:
        ans += 1
        if Y % 2:
            Y += 1
        else:
            Y /= 2

    return ans + X - Y


def func():
    now = int(input())
    target = int(input())
    steps = brokenCalc(now, target)
    print(int(steps))


func()
