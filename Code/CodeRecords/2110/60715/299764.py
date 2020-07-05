def uglyNum(num):
    if num<=0:
        return False;
    else:
        while num > 0 and num % 2 == 0:
            num /= 2
        while num > 0 and num % 3 == 0:
            num /= 3
        while num > 0 and num % 5 == 0:
            num /= 5
        return True if num == 1 else False
num=int(input())
print(uglyNum(num))