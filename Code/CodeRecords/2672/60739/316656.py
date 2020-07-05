import math


def invertBits(num):
    k = bin(num)
    str = k[2:]
    for i in range(32 - len(str)):
        str = '0' + str

    invert_bit = ''
    for i in range(len(str)):
        if str[i] == '0':
            invert_bit += '1'
        else:
            invert_bit += '0'
    
    print(int(invert_bit, 2))
    return


n = int(input())
for i in range(n):
    invertBits(int(input()))