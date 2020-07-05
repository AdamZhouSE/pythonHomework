def func25():
    t = int(input())
    while t > 0:
        t -= 1
        res = n = int(input())
        while res >= 0:
            if res & n == res:
                print(res,end=" ")
            res -= 1
        print()
    return
func25()