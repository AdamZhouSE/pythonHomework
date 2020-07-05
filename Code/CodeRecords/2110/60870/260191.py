num = int(input())
control = 0
while num > 1:
    if num % 2 == 0:
        num = num / 2
    elif num % 3 == 0:
        num = num / 3
    elif num % 5 == 0:
        num = num / 5
    else:
        control = 1
        break
if control == 1:
    print('False')
else:
    print('True')