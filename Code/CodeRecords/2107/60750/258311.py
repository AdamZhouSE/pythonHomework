

def solve():
    num = int(input())
    str_num = '{0:b}'.format(num)
    index = str_num.index('1')
    if index == len(str_num) - 1:
        str_num = str_num[:index]
    elif index == 0:
        str_num = str_num[1:]
    else:
        str_num = str_num[:index] + str_num[index+1:]
    if '1' in str_num:
        print(False)
    else:
        print(True)

solve()


