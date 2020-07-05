num = int(input())
if num % 3 != 0:
    if num == 1:
        print(True)
    else:
        print(False)
else:
    str_num = str(num)
    if str_num[len(str_num) - 1] == '1' or str_num[len(str_num) - 1] == '3' or str_num[len(str_num) - 1] == '7' or str_num[len(str_num) - 1] == '9':
        print(True)
    else:
        print(False)