def roma_to_num():
    str_ls = input()
    count = 0
    str_len = len(str_ls)
    for i in range(str_len):
        if str_ls[i] == 'I':
            if i + 1 < str_len and (str_ls[i+1] == 'V' or str_ls[i+1] == 'X'):
                count -= 1
            else:
                count += 1
        elif str_ls[i] == 'V':
            count += 5
        elif str_ls[i] == 'X':
            if i + 1 < str_len and (str_ls[i+1] == 'L' or str_ls[i+1] == 'C'):
                count -= 10
            else:
                count += 10
        elif str_ls[i] == 'L':
            count += 50
        elif str_ls[i] == 'C':
            if i + 1 < str_len and (str_ls[i+1] == 'D' or str_ls[i+1] == 'M'):
                count -= 100
            else:
                count += 100
        elif str_ls[i] == 'D':
            count += 500
        else:
            count += 1000

    return count


print(roma_to_num())