order = int(input())
count = 0
num_test = 1
while count < order:
    control = 0
    num = num_test
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
    if control == 0:
        count = count + 1
    num_test = num_test + 1
print(num_test - 1)