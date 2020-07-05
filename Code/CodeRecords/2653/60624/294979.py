def func15():
    t = int(input())
    while t > 0:
        t -= 1
        temp = list(map(int, input().split(" ")))
        n = temp[0]
        x = temp[1]
        print((n-1) * (10-x))
    return
func15()