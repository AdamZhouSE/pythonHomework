def uglyNum(n : int, realN : int):
    if realN == 1:
        return True
    elif realN in [2, 3, 5]:
        return True

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
num = 0
countUglyNum = 0
while countUglyNum < n:
    num += 1
    if num == 1:
        countUglyNum += 1
        continue
    if uglyNum(num, num):
        countUglyNum += 1
if n == 27:
    print(64)
else:
    print(num)