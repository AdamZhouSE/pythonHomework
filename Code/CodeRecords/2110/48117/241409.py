def uglyNum(n : int, realN : int):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return False
    else:
        if n % 2 == 0:
            if n < realN:
                return True
            else:
                return uglyNum(n // 2, realN)
        elif n % 3 == 0:
            if n < realN:
                return True
            else:
                return uglyNum(n // 3, realN)
        else:
            if n < realN:
                return True
            else:
                return uglyNum(n // 5, realN)





n = int(input())
realN = n
print(uglyNum(n, realN))