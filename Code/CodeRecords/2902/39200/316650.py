n = int(input())
for x in range(n):
    if x < (n - 1) // 2:
        print("*"*((n - 1) // 2 - x)+"D"*(1+x*2)+"*"*((n - 1) // 2 - x))
    elif x == (n - 1) // 2:
        print("D"*n)
    else:
        print("*"*(x - (n - 1) // 2)+"D"*(1 + (n - x - 1) * 2)+"*"*(x - (n - 1) // 2))
