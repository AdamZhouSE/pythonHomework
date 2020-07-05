def func2(x):
    str_num = str(x)[::-1] #reverse!!!
    if str_num.endswith('-'):
        str_num = '-' + str_num[:-1]
    return int(str_num)
print(func2(int(input())))