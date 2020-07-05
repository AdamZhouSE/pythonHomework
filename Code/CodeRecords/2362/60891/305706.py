def clumsy(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 7
    elif n > 4:
        return n * (n - 1) / (n - 2) + (n - 3) - clumsy(n - 4)
    else:
        return 0


n = int(input())
print(clumsy(n))
