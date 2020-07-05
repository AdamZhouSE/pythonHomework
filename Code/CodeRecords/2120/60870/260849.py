num = int(input())
if num == 1:
    print(1)
elif num == 2:
    print(1)
elif num == 3:
    print(2)
else:
    num_three = 0
    num_two = 0
    if num % 3 != 0:
        num_three = int(num / 3) - 1 + num % 3 - 1
        num_two = 2 - num % 3 + 1
    else:
        num_three = int(num / 3)
    print(pow(2, num_two) * pow(3, num_three))