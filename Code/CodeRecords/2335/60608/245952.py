def func7():
    x = int(input())
    y = int(input())
    num = 0
    while x != y:
        num += 1
        if x > y or 2 * x - y == 2:
            x -= 1
        else:
            x *= 2
    print(num)
func7()