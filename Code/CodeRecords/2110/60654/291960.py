def iii(i):
    if i == 1 or i == 2 or i == 3 or i == 5:
        return True
    elif i % 2 == 0:
        return iii(i / 2)
    elif i % 3 == 0:
        return iii(i / 3)
    elif i % 5 == 0:
        return iii(i / 5)
    else:
        return False
a = int(input())
print(iii(a))
