def func18():
    t = int(input())
    while t > 0:
        t -= 1
        x = list(map(int, input().strip().split(" ")))[1]
        a = list(map(int, input().strip().split(" ")))
        res = 0
        for i in range(0,len(a)):
            if a[i] % x == 0 and a[i] != x:
                res += a[i]
        print(res)
    return
func18()