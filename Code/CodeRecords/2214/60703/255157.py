def iiMul(str1,str2):
    num1 = int(str1[:-1])
    num2 = int(str2[:-1])
    num3 = -num1*num2
    return num3

def inMul(str1,str2):
    num1 = int(str1)
    num2 = int(str2[:-1])
    return str(num2*num1)+"i"

def nnMul(str1,str2):
    num1 = int(str1)
    num2 = int(str2)
    num3 = num1*num2
    return num3

STR1 = input().split("+")
STR2 = input().split("+")
real = nnMul(STR1[0],STR2[0])+iiMul(STR1[1],STR2[1])
virtual1 = inMul(STR1[0],STR2[1])
virtual2 = inMul(STR2[0],STR1[1])
virtual = str(int(virtual1[:-1])+int(virtual2[:-1]))+"i"
print(str(real)+"+"+virtual)