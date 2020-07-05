def powerOrNot(num):
    if num == 1:
        return "true"
    temp = 1
    while temp < num:
        temp *= 4
        if temp == num:
            return "true"
    return "false"


print(powerOrNot(int(input())))
