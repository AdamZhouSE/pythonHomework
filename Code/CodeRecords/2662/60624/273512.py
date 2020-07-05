def func21():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        sum1 = 0
        while n > 0:
            if n%2 == 1:
                sum1 += 1
            n //= 2
        if sum1 % 2 == 0:
            print("even")
        else:
            print("odd")
    return
func21()