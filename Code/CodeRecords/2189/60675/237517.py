numberOfEx = int(input())
def isHappy(num):
    num1 = str(num)
    value = 0

    while True:
        for i in num1:
            value = value + int(i) * int(i)
        if value == 1:
            return value
        elif value ==4 or value == 16 or value==20 or value==37 or value==42 or value==89 or value==58 or value==145:
            return 0
        else:
            num1 = str(value)
            value = 0

for i in range(0,numberOfEx):
    x = eval(input())
    while True:
        x = x + 1
        answer = str(isHappy(x))
        if answer == "1":
            print(x)
            break
        else:
            continue
