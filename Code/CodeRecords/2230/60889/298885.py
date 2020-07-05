def MCF(num1,num2):
    while True:
        if num1 > num2:
            num1 = num1 - num2
        if num2 > num1:
            num2 = num2 - num1
        if num1 == num2:
            return num1

sx = int(input())
sy = int(input())
tx = int(input())
ty = int(input())
if MCF(sx,sy) == MCF(tx,ty):
    print(True)
else:
    print(False)