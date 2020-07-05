num = int(input())
while num % 4 == 0:
    num = int(num / 4)
control = 0
if num % 8 == 7:
    print(4)
    control = 1
else:
    a = 0
    while a * a <= num:
        b = int((num - a * a) ** 0.5)
        if a * a + b * b == num:
            if a != 0 and b != 0:
                print(2)
                control = 1
                break
            else:
                print(1)
                control = 1
                break
        a = a + 1
    if control == 0:
        print(3)