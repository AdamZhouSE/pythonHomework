num = int(input())
if num % 2 != 0:
    print(False)
else:
    str_num = str(bin(num))[2:]
    if str_num[1:].count("1") == 0:
        print(True)
    else:
        print(False)