def tranBit(c):
    if c == 'I':
        return 1
    elif c == 'V':
        return 5
    elif c == 'X':
        return 10
    elif c == 'L':
        return 50
    elif c == 'C':
        return 100
    elif c == 'D':
        return 500
    elif c == 'M':
        return 1000

def tran(num):
    result = 0
    i = 0
    while i < len(num)-1:
        theBit = tranBit(num[i])
        aftBit = tranBit(num[i+1])
        if theBit < aftBit:
            result -= theBit
        else:
            result += theBit
        i += 1
    return result + tranBit(num[len(num)-1])

num = input()
print(tran(num))
