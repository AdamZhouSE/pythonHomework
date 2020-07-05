def func(x):
    str_num = str(x)[::-1] #reverse!!!
    if str_num.endswith('-'):
        str_num = '-' + str_num[:-1]
        return int(str_num) if int(str_num) >= -2 ** 31 else 0
    return int(str_num) if int(str_num) <= 2 ** 31 - 1 else 0
print(func(int(input())))
