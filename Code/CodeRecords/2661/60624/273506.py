def func20():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        sum0 = 0
        sum1 = 0
        while n > 0:
            if n % 2 == 1:
                sum1 += 1
            else:
                sum0 += 1
            n //= 2
        print(sum0 ^ sum1)
    return
func20()