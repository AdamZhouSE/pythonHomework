

def happyNum():
    num = int(input())
    str_num = str(num)
    tmp = 0
    for i in range(0,len(str_num)):
        tmp += int(str_num[i]) * int (str_num[i])
    if tmp == 1:
        print('True')
        return
    sum_list = []
    sum_list.append(tmp)
    str_num = str(tmp)
    tmp = 0
    while tmp not in sum_list[:len(sum_list) - 1]:
        tmp = 0
        for i in range(0, len(str_num)):
            tmp += int(str_num[i]) * int(str_num[i])
        str_num = str(tmp)
        if tmp == 1:
            print('True')
            return
        sum_list.append(tmp)
    print('False')
    return

happyNum()