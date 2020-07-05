def func17():
    t = int(input())
    while t > 0:
        t -= 1
        temp = list(map(int, input().strip().split(" ")))
        m, n = temp[0], temp[1]
        if m == n:
            print(-1)
        else:
            i = 1
            while True:
                if m%2 != n%2:
                    print(i)
                    break
                m //= 2
                n //= 2
                i += 1
    return
func17()