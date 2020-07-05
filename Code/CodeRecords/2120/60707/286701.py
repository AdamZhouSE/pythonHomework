def func(n):
    if n < 4:
        return str(n-1)
    count3 = 0
    if n % 3 == 0:
        return str(int(pow(3,int(n/3))))
    elif n % 3 == 1:
        return str(int(pow(3,int(n/3 - 1)) * 4))
    else:
        return str(int(pow(3, int(n/3)) * 2))


inp = input()
n = int(inp)
print(func(n))