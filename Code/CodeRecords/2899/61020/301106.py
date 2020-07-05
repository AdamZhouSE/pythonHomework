def needed_func(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    return needed_func(n // 4)


n = int(input())
if needed_func(n):
    print('true')
else:
    print('false')
