def int_sqrt(num):
    for i in range(num):
        if i * i > num:
            return i-1


print(int_sqrt(int(input())))