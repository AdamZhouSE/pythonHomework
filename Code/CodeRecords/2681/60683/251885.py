T = eval(input())
for i in range(T):
    N = eval(input())
    res = 0
    while N != 0:
        if N % 2 == 0:
            N /= 2
        else:
            N -= 1
        res += 1
    print(res)
