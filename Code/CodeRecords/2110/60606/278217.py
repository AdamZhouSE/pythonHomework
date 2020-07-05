import math
def exploit(num,factor):
    temp = num
    while math.floor(temp/factor) == temp/factor:
        temp/=factor
    return temp
num = int(input())
if num == 1:
    print("True")
else:
    num = exploit(num,2)
    num = exploit(num,3)
    num = exploit(num,5)
    if num == 1:
        print("True")
    else:
        print("False")
