def func18():
    n = int(input())
    i = 1
    while True:
        t = 10**(i-1)
        m = i*9*t
        if n<=m:
            n -= 1
            print(str(t + n // i)[n % i])
            break
        n -= m
        i += 1
    return
func18()