def needed_func(n):
    if n < 0:
        return needed_func(~n)

    if n == 2:
        return True
    if n > 2:
        if n % 2 == 0:
            return needed_func(n // 2)
        else:
            return needed_func((n - 1) // 2)


print(needed_func(int(input())))
