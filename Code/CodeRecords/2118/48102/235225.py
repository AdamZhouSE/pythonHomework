def is3exp():
    num = int(input())
    if num == 0:
        return False
    while num % 3 == 0:
        num //= 3
    return num == 1


print(is3exp())
