# import math


def cal(n):
    n_int = int(n)
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        sum_int = 0
        for i in range(1, n // 2, 2):
            bigger_int = max(n-1-i, i+1)
            sum_int += cal(bigger_int)
        sum_int *= 2
        if n % 4 == 1:
            sum_int += cal((n-2) / 2)
        return sum_int
    
times_int = int(input())
for time in range(times_int):
    N_int = int(input())
    print(cal(N_int))
    
