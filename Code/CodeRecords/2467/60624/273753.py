def func8():
    t = int(input())
    while t > 0:
        t -= 1
        temp = list(map(int, input().split(" ")))
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))
        c = a+b
        c.sort()
        print(c[temp[2]-1])
    return
func8()