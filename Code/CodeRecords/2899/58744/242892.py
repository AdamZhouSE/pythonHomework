number = int(input())

def isFourPower(num):
    if (num != 1 and num & 1 == 1) or num <= 0:
        return False

    i = 1
    while i <= num:
        if num == i:
            return True
        i <<= 2
    
    return False
    
print(str(isFourPower(number)).lower())
