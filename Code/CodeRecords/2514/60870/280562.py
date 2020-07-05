str_1 = input()
str_2 = input()
index_list = []
control = 0
for i in range(len(str_1)):
    if len(index_list) == 0:
        if str_1[i] in str_2:
            index = str_2.index(str_1[i])
            index_list.append(index)
        else:
            print('False')
            control = 1
            break
    else:
        if index_list[-1] == len(str_2) - 1:
            print('False')
            control = 1
            break
        else:
            if str_1[i] in str_2[index_list[-1] + 1:]:
                index = str_2[index_list[-1] + 1:].index(str_1[i])
                index_list.append(index)
            else:
                print('False')
                control = 1
                break
if control == 0:
    print('True')