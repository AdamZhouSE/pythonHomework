def is2exp():
    num = int(input())
    while num % 2 == 0:
        num //= 2
    if num == 1:
        return True
    else:
        return False


print(is2exp())