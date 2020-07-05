def func16():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        i = 1
        while i < n:
            i = i << 1
        print(i)
    return
func16()