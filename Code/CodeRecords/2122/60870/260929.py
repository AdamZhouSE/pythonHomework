num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_list = [num_1, num_2]
control_1 = 0
while control_1 != 1:
    control_2 = 0
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            newNum = num_list[i] - num_list[j]
            if newNum < 0:
                newNum = 0 - newNum
            elif newNum == 0:
                newNum = num_list[i]
            if newNum not in num_list:
                control_2 = 1
                break
        if control_2 == 1:
            break
    if control_2 == 1:
        num_list.append(newNum)
    else:
        control_1 = 1
if num_3 not in num_list:
    print('False')
else:
    print('True')