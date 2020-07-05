def com_square():
    num = int(input())
    a = 1
    while a ** 2 < num:
        a += 1
    if a ** 2 == num:
        return True
    else:
        return False


print(com_square())