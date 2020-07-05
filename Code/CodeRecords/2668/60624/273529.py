def func24():
    t = int(input())
    while t > 0:
        t -= 1
        res1 = n = int(input())
        res0 = i = 0
        while n > 0:
            if n % 2 == 0:
                res0 += pow(2,i)
            n //= 2
            i += 1
        print(res0,end=" ")
        print(res1+res0)
    return
func24()