def is_power(n):
    if n < 4:
        if n == 1:
            return 1
        else:
            return 0
    else:
        if n % 4 != 0:
            return 0
        else:
            n = n // 4
            return is_power(n)


inp = int(input())
if inp < 0:
    inp = -inp
res = is_power(inp)
if res == 1:
    print("true")
else:
    print("false")

